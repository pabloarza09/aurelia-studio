'use client';

import { useEffect, useState } from 'react';
import { fetchOrders, Order } from '../services/api';
import { OrdersTable } from '../components/OrdersTable';

export default function DashboardPage() {
  const [orders, setOrders] = useState<Order[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    async function loadData() {
      const data = await fetchOrders();
      setOrders(data);
      setLoading(false);
    }
    loadData();
    
    // Opcional: Polling cada 10 segundos para simular tiempo real en desarrollo
    const interval = setInterval(loadData, 10000);
    return () => clearInterval(interval);
  }, []);

  return (
    <main className="min-h-screen bg-gray-50 p-8">
      <div className="mx-auto max-w-6xl space-y-6">
        <header className="flex flex-col gap-1">
          <h1 className="text-3xl font-bold tracking-tight text-gray-900">Aurelia OS Dashboard</h1>
          <p className="text-sm text-gray-500">Monitoreo omnicanal y flujo de agentes en tiempo real</p>
        </header>

        {loading ? (
          <div className="flex h-32 items-center justify-center text-sm text-gray-500">
            Cargando flujo de datos del monorepo...
          </div>
        ) : (
          <div className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm space-y-4">
            <h2 className="text-lg font-semibold text-gray-900">Ventas Recientes</h2>
            <OrdersTable orders={orders} />
          </div>
        )}
      </div>
    </main>
  );
}