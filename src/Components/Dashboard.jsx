import React, { useState, useEffect } from 'react';
import axios from 'axios';

/**
 * Dashboard component for displaying transaction data.
 *
 * @component
 * @example
 * // Usage
 * <Dashboard />
 */
const Dashboard = () => {
  const [transactions, setTransactions] = useState([]);
  const [filters, setFilters] = useState({});

  useEffect(() => {
    fetchTransactions();
  }, [filters]);

  const fetchTransactions = async () => {
    const response = await axios.get('/transactions/search', { params: filters });
    setTransactions(response.data);
  };

  const handleFilterChange = (e) => {
    setFilters({ ...filters, [e.target.name]: e.target.value });
  };

  return (
    <div>
      <h1>Transaction Dashboard</h1>
      <div>
        <input name="amount" placeholder="Amount" onChange={handleFilterChange} />
        <input name="date_from" placeholder="Date From" onChange={handleFilterChange} />
        <input name="date_to" placeholder="Date To" onChange={handleFilterChange} />
        <input name="description" placeholder="Description" onChange={handleFilterChange} />
      </div>
      <table>
        <thead>
          <tr>
            <th>Transaction ID</th>
            <th>Amount</th>
            <th>Description</th>
            <th>Date/Time</th>
            <th>User ID</th>
            <th>Country</th>
            <th>Tags</th>
          </tr>
        </thead>
        <tbody>
          {transactions.map(t => (
            <tr key={t.transaction_id}>
              <td>{t.transaction_id}</td>
              <td>{t.amount}</td>
              <td>{t.description}</td>
              <td>{t.date_time}</td>
              <td>{t.user_id}</td>
              <td>{t.country}</td>
              <td>{t.tags}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Dashboard;