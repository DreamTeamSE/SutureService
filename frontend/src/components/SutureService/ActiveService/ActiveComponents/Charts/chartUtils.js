export const generateTimeLabels = (metrics) => {
  if (!metrics) return [];
  return metrics.points.map((_, index) => 
    `2024-01-01T00:00:${String(index).padStart(2, '0')}`
  );
};

export const getChartName = (selected, Status) => {
  if (selected === Status.ACCELERATION) {
    return Status.ACCELERATION;
  }
  return Status.VELOCITY;
}; 