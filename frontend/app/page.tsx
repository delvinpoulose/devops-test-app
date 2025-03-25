'use client';

import { useEffect, useState } from 'react';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL;

export default function HomePage() {
  const [hostname, setHostname] = useState('');
  const [loading, setLoading] = useState(false);

  const fetchHostname = async () => {
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE_URL}/hostname`);
      const data = await res.json();
      setHostname(data.hostname);
    } catch (error) {
      console.error('Error fetching hostname:', error);
      setHostname('Error fetching hostname');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchHostname();
  }, []);

  return (
    <main style={{ padding: '2rem' }}>
      <h1>Server Hostname</h1>
      <button onClick={fetchHostname} disabled={loading}>
        {loading ? 'Loading...' : 'Get Hostname'}
      </button>
      <p style={{ fontSize: '1.5rem', marginTop: '1rem' }}>
        {hostname ? `Hostname: ${hostname}` : 'No response yet'}
      </p>
    </main>
  );
}

