import { useEffect, useState } from "react";
import axios from "axios";
import { Bar } from "react-chartjs-2";

export default function JobTrendChart() {
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    axios.get("/api/trend/skills").then((res) => {
      const data = res.data.items;

      // 예시: 백엔드 직무만 필터링
      const backendData = data.filter(item => item.job_type === "backend");
      const labels = backendData.map(d => d.tech_stack);
      const frequencies = backendData.map(d => d.frequency);

      setChartData({
        labels,
        datasets: [{
          label: "Backend 기술 빈도",
          data: frequencies,
          backgroundColor: "rgba(75, 192, 192, 0.6)"
        }]
      });
    });
  }, []);

  return chartData ? (
    <div style={{ width: "600px" }}>
      <Bar data={chartData} />
    </div>
  ) : (
    <p>로딩 중...</p>
  );
}
