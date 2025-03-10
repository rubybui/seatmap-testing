import SeatToolkit from "@mezh-hq/react-seat-toolkit";
import "@mezh-hq/react-seat-toolkit/styles";
import seats from "./seattoolkit.json";
import { Armchair } from "lucide-react";

const ReactToolKitSeat = () => {

    return (
        <div style={{ width: "1000px", height: "1000px" }}>
            <SeatToolkit
                mode={"user"}
                data={seats}
            />
        </div>);
};
export default ReactToolKitSeat;