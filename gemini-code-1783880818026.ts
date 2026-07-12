import React from 'react';
import { Order } from '../services/api';

interface OrdersTableProps {
  orders: Order[];
}

export const OrdersTable: React.FC<OrdersTableProps> = ({ orders }) => {
  return (
    <div className="overflow-x-auto rounded-lg border border-gray-200 shadow-sm">
      <table className="min-w-full divide-y divide-gray-200 bg-white text-sm">
        <thead className="bg-gray-50 text-left font-medium text-gray-900">
          <tr>
            <th className="px-4 py-3">ID Orden</th>
            <th className="px-4 py-3">Plataforma</th>
            <th className="px-4 py-3">Producto</th>
            <th className="px-4 py-3">Cliente</th>
            <th className="px-4 py-3 text-right">Total</th>
          </tr>
        </thead>
        <tbody className="divide-y divide-gray-200 text-gray-700">
          {orders.length === 0 ? (
            <tr>
              <td colSpan={5} className="px-4 py-8 text-center text-gray-400">
                No hay ventas registradas aún. Esperando webhooks...
              </td>
            </tr>
          ) : (
            orders.map((order) => (
              <tr key={order.id} className="hover:bg-gray-50 transition-colors">
                <td className="px-4 py-3 font-mono font-medium text-blue-600">{order.id}</td>
                <td className="px-4 py-3">
                  <span className="inline-flex items-center rounded-md bg-purple-50 px-2 py-1 text-xs font-medium text-purple-700 ring-1 ring-inset ring-purple-700/10">
                    {order.platform}
                  </span>
                </td>
                <td className="px-4 py-3 text-gray-900">{order.product_id}</td>
                <td className="px-4 py-3">{order.customer_email}</td>
                <td className="px-4 py-3 text-right font-semibold text-gray-950">
                  {order.price_paid.toFixed(2)} {order.currency}
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
};