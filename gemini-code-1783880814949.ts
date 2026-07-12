export interface Order {
  id: string;
  platform: string;
  product_id: string;
  customer_email: string;
  price_paid: number;
  currency: string;
  created_at: string;
}

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export async function fetchOrders(): Promise<Order[]> {
  try {
    const response = await fetch(`${API_URL}/api/v1/orders`);
    if (!response.ok) {
      throw new Error('Error al obtener las órdenes del backend');
    }
    return await response.json();
  } catch (error) {
    console.error("API Error:", error);
    return [];
  }
}