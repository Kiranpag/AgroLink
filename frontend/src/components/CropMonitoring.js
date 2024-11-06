import React, { useState, useEffect } from 'react';
import { getCropHealth } from '../api';

function CropMonitoring() {
  const [cropHealth, setCropHealth] = useState(null);

  useEffect(() => {
    const fetchHealth = async () => {
      const data = await getCropHealth("sample_sensor_data");
      setCropHealth(data.crop_health);
    };
    fetchHealth();
  }, []);

  return (
    <div>
      <h2>Crop Monitoring</h2>
      <p>Crop Health: {cropHealth}</p>
    </div>
  );
}

export default CropMonitoring;
