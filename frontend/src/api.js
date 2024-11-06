export async function getCropHealth(sensorData) {
    const response = await fetch(`/api/crop/health?sensor_data=${sensorData}`);
    return await response.json();
  }
  
  export async function initiateTransaction(transactionData) {
    const response = await fetch(`/api/marketplace/transaction`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(transactionData)
    });
    return await response.json();
  }
  