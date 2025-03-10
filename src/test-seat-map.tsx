import { useRef } from 'react';
import Seatmap, { SeatmapRef } from '@alisaitteke/seatmap-canvas-react';

const MySeatmapComponent = () => {
  // Explicitly type the ref with SeatmapRef
  const seatmapRef = useRef<SeatmapRef>(null);

  const seatClick = (seat: any) => {
    if (!seat.isSelected() && seat.item.salable === true) {
      seat.select();
    } else {
      seat.unSelect();
    }
  };

  const handleGetSelectedSeats = () => {
    if (seatmapRef.current) {
      const selectedSeats = seatmapRef.current.getSelectedSeats();
      console.log('Selected seats:', selectedSeats);
    }
  };

  const config = {
    resizable: true,
    legend: true,
    style: {
      seat: {
        hover: '#8fe100',
        color: '#f0f7fa',
        selected: '#8fe100',
        check_icon_color: '#fff',
        not_salable: '#0088d3',
        focus: '#8fe100',
        radius: 12,
      },
      legend: {
        font_color: '#3b3b3b',
        show: false,
      },
      block: {
        title_color: '#fff',
      },
    },
  };

const blocks = [
  {
    id: 1,
    title: 'Test Block 1',
    color: '#2c2828',
    labels: [
      { title: 'A', x: -30, y: 0 },
      { title: 'B', x: 120, y: 30 },
    ],
    seats: [
      { id: 1, x: 0, y: 0, salable: true, note: 'note test', title: '49' },
      { id: 2, x: 30, y: 0, salable: true, note: 'note test', title: '47' },
    ],
  },
];

  return (
    <div style={{ width: '100%', height: '100vh' }}>
      <Seatmap
        ref={seatmapRef}
        className="w-full flex-1 h-full"
        seatClick={seatClick}
        blocks={blocks}
        config={config}
      />
      <button onClick={handleGetSelectedSeats} style={{ marginTop: '20px' }}>
        Get Selected Seats
      </button>
    </div>
  );
};

export default MySeatmapComponent;
