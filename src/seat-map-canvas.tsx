import * as React from 'react';
import { Seatmap as OriginalSeatmap } from '@alisaitteke/seatmap-canvas-react';

interface VenueSeatmapCreatorProps {
  // Define any props you need here
}

interface VenueSeatmapCreatorState {
  val: string;
}

export class VenueSeatmapCreator extends React.Component<
  VenueSeatmapCreatorProps,
  VenueSeatmapCreatorState
> {
  private seatmapRef = React.createRef<OriginalSeatmap>();

  constructor(props: VenueSeatmapCreatorProps) {
    super(props);
    this.state = { val: '' };
  }

  componentDidMount(): void {
    if (this.seatmapRef.current) {
      // Called right after the component mounts
      console.log('Seatmap is mounted and accessible', this.seatmapRef.current);
    }
  }

  zoomToVenue(): void {
    // Exposes the seatmap's zoomToVenue function (if the library has it)
    this.seatmapRef.current?.zoomToVenue();
  }

  handleSeatClick = (seat: any) => {
    // Example seat-click logic
    if (!seat.isSelected() && seat.item.salable === true) {
      seat.select();
    } else {
      seat.unSelect();
    }
  };

  handleGetSelectedSeats = () => {
    const selectedSeats = this.seatmapRef.current?.getSelectedSeats();
    console.log('Selected seats:', selectedSeats);
  };

  render(): React.ReactNode {
    const config = {
      legend: true,
      style: {
        seat: {
          hover: '#8fe100',
          color: '#f0f7fa',
          selected: '#8fe100',
          check_icon_color: '#fff',
          not_salable: '#0088d3',
          focus: '#8fe100',
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
        title: 'Block 1',
        color: '#2c2828',
        blockX: 0,
        blockY: 0,
        labels: [
          { title: 'A', x: -30, y: 0 },
          { title: 'B', x: 120, y: 30 },
        ],
        seats: [
          { id: 1, x: 0, y: 0, salable: true, note: 'note test', title: '49' },
          { id: 2, x: 30, y: 0, salable: true, note: 'note test', title: '47' },
        ],
      },
      {
        id: 2,
        title: 'Block 2',
        color: '#2c2828',
        blockX: 200,
        blockY: 100,
        labels: [
          { title: 'A', x: -30, y: 0 },
          { title: 'B', x: 120, y: 30 },
        ],
        seats: [
          { id: 3, x: 0, y: 0, salable: true, note: 'note test', title: '49' },
          { id: 4, x: 30, y: 0, salable: true, note: 'note test', title: '47' },
        ],
      },
    ];

    return (
      <div style={{ width: '1000px', height: '1000px' }}>
        {/* The OriginalSeatmap component */}
        <OriginalSeatmap
          ref={this.seatmapRef}
          seatClick={this.handleSeatClick}
          blocks={blocks}
          config={config}
        />

        <button onClick={this.handleGetSelectedSeats} style={{ marginTop: '20px' }}>
          Get Selected Seats
        </button>
        <button onClick={() => this.zoomToVenue()} style={{ marginLeft: '10px' }}>
          Zoom to Venue
        </button>

        <p>{this.state.val}</p>
      </div>
    );
  }
}

export default VenueSeatmapCreator;
