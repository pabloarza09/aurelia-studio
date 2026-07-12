from fastapi import FastAPI, Depends, HTTPException, Status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from security import verify_password, create_access_token
import logging

app = FastAPI(title="Aurelia OS - API Core con Seguridad JWT")
logger = logging.getLogger("AureliaOS-Auth")

# Base de datos simulada de usuarios administrativos para la fase v0.2
USER_DB = {
    "admin@aurelia.studio": {
        "username": "admin@aurelia.studio",
        # El hash de la contraseña 'aurelia2026' generado por seguridad
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36XKp7f6A7B13uGj3KOWG3K", 
        "role": "CEO"
    }
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

@app.post("/api/v1/auth/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Endpoint de Login que valida las credenciales y devuelve el JWT"""
    user = USER_DB.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=Status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Generamos el token de acceso con el rol del usuario corporativo
    access_token = create_access_token(data={"sub": user["username"], "role": user["role"]})
    logger.info(f"[Auth] Sesión iniciada con éxito para: {user['username']}")
    
    return {"access_token": access_token, "token_type": "bearer"}