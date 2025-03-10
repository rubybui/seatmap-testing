import SeatToolkit, { store, actions }  from "@mezh-hq/react-seat-toolkit";
import "@mezh-hq/react-seat-toolkit/styles";
import seats_array from "./seats.json";
import texts from "./texts.json";
import { Armchair } from "lucide-react";
import { IPopulatedSeat,ISeat } from "@mezh-hq/react-seat-toolkit/types";
import { useState } from "react";

const ReactToolKitSeat = () => {
    const [seats, setSeats] = useState<ISeat[]>(seats_array as ISeat[]);

    const onSeatClick = (clickedSeat: IPopulatedSeat) => {
        // Update the seat’s status to "Reserved"
        setSeats((prevSeats) =>
          prevSeats.map((seat) =>
            seat.id === clickedSeat.id
              ? { ...seat, status: 'Reserved' }
              : seat
          )
        );
        console.log(seats)
      };
    return (
        <div style={{ width: "1000px", height: "1000px" }}>
            <SeatToolkit
                mode={"user"}
                data={{
                    name: "Categorized Example",
                    categories: [
                        {
                            id: 'zone1',
                            name: 'Zone 1',
                            color: '#B60208',
                            textColor: '#fff',
                          },
                          {
                            id: 'zone2',
                            name: 'Zone 2',
                            color: '#F99446',
                            textColor: '#fff',
                          },
                          {
                            id: 'zone3',
                            name: 'Zone 3',
                            color: '#EADD1C',
                            textColor: '#fff',
                          },
                          {
                            id: 'zone4',
                            name: 'Zone 4',
                            color: '#1EB0EF',
                            textColor: '#fff',
                          },
                          {
                            id: 'zone5',
                            name: 'Zone 5',
                            color: '#0FAD4F',
                            textColor: '#fff',
                          },
                    ],
                    sections: [
                        {
                            id: "1636dd75-ea0a-48d6-b14c-05ac9db08f5c",
                            name: "Section 1",
                            color: "#000000",
                            stroke: "#000000",
                            freeSeating: false
                        },
                        {
                            id: "65dfc91f-f7aa-407a-ae55-b31f1ee3a41c",
                            name: "Section 2",
                            color: "#FF0000",
                            stroke: "#FF0000",
                            freeSeating: false
                        },
                        {
                            id: "6975d973-5a37-4490-bf13-85c156cbb6b3",
                            name: "Section 3",
                            color: "#0000FF",
                            stroke: "#0000FF",
                            freeSeating: false
                        }
                    ],
                    seats: seats_array ,
                    text: texts,
                    shapes: [
                        {
                            id: "60a1c8d8-efd1-4506-a5a8-59ef16571836",
                            name: "RectangleHorizontal",
                            x: 117.017578125,
                            y:  -69.24331676483155,
                            width: 1100,
                            height: 100,
                            rx: 10,
                            color: "#000000",
                            stroke: "#000000"
                        }
                    ],
                    polylines: [],
                    images: [],
                    workspace: { initialViewBoxScale: 0.605909115101895, initialViewBoxScaleForWidth: 1386, visibilityOffset: 0 }

                }}
                options={{
                    shapes: {
                        icons: [
                            Armchair
                        ],
                        overrideDefaultIconset: true
                    }
                }}
                events={{
                    onSeatClick: onSeatClick,
                  }}
            />
        </div>);
};
export default ReactToolKitSeat;