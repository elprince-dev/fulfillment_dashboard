'use client';
import { useEffect, useState } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';

// Registering the necessary chart.js components
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const Dashboard = () => {
  const [inventoryData, setInventoryData] = useState([]);
  const [defectData, setDefectData] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/inventory').then((res) => {
      setInventoryData(res.data);
    });
    axios.get('http://127.0.0.1:8000/defects').then((res) => {
      setDefectData(res.data);
    });
  }, []);

  // Chart data for inventory vs defect statistics
  const inventoryChartData = {
    labels: inventoryData.map(item => item.product_name),
    datasets: [
      {
        label: 'Quantity in Stock',
        data: inventoryData.map(item => item.quantity_in_stock),
        borderColor: '#34D399', // Soft green
        backgroundColor: 'rgba(52, 211, 153, 0.2)', // Light green fill
        tension: 0.1,
      },
      {
        label: 'Quantity Defective',
        data: inventoryData.map(item => item.quantity_defective),
        borderColor: '#EF4444', // Bright red
        backgroundColor: 'rgba(239, 68, 68, 0.2)', // Light red fill
        tension: 0.1,
      },
    ],
  };

  return (
    <div className="bg-gray-100 min-h-screen flex flex-col items-center justify-center text-gray-800 py-8 px-4">
      {/* Title */}
      <h1 className="text-3xl font-semibold text-center text-gray-900 mb-8">
        Fulfillment Operations Dashboard
      </h1>

      {/* Chart Section */}
      <div className="w-full max-w-4xl bg-white p-6 rounded-xl shadow-lg mb-10">
        <h2 className="text-xl font-semibold text-center text-gray-700 mb-6">Inventory vs Defect Statistics</h2>
        <div className="w-full">
          <Line data={inventoryChartData} />
        </div>
      </div>

      {/* Footer */}
      <footer className="w-full text-center text-sm text-gray-500 mt-8">
        <p>elprince.net</p>
      </footer>
    </div>
  );
};

export default Dashboard;
