import React from 'react';

const matrix = [
    [
        0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1,
        1, 1, 1, 0, 0,
    ], // side walks and seats
    [
        0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1,
        1, 1, 1, 0, 0,
    ], // middle aisle
    [
        0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1,
        1, 1, 1, 0, 0,
    ], // side walks and seats
    [
        0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1,
        1, 1, 1, 0, 0,
    ], // side walks and seats
    [
        0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1,
        1, 1, 1, 0, 0,
    ], // middle aisle
    [
        0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1,
        1, 1, 1, 0, 0,
    ], // side walks and seats
    [
        0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1,
        1, 1, 1, 0, 0,
    ], // side walks and seats
    [
        0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1,
        0, 0, 1, 0, 0,
    ], // middle aisle
    [
        0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1,
        1, 1, 1, 0, 0,
    ], // side walks and seats
    [
        0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1,
        1, 1, 1, 0, 0,
    ], // side walks and seats
    [
        0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1,
        0, 0, 1, 0, 0,
    ], // middle aisle
    [
        0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1,
        1, 1, 1, 0, 0,
    ], // side walks and seats
    [
        0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1,
        1, 1, 1, 0, 0,
    ], // side walks and seats
]

const CinemaHall: React.FC = () => {
    // Define inline styles
    const parentStyle: React.CSSProperties = {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    };

    const containerStyle: React.CSSProperties = {
        display: 'flex',
        margin: '2px',
    };

    const itemBaseStyle: React.CSSProperties = {
        width: '10px',
        height: '10px',
        margin: '1px',
        borderWidth: '1px',
        borderStyle: 'solid',
        borderRadius: '2px',
        borderColor: 'white',
    };

    const seatStyle: React.CSSProperties = {
        ...itemBaseStyle,
        borderColor: 'black',
        backgroundColor: 'green',
    };

    const spaceStyle: React.CSSProperties = {
        ...itemBaseStyle,
        backgroundColor: 'lightgray',
    };

    const screenStyle: React.CSSProperties = {
        border: '1px solid black',
        padding: '5px',
        borderRadius: '5px',
        display: 'flex',
        justifyContent: 'center',
        marginTop: '5px',
    };

    return (
        <div>
            <div id="parent" style={parentStyle}>
                {matrix.map((row, rowIndex) => (
                    <div key={`row-${rowIndex}`} style={containerStyle}>
                        {row.map((element, seatIndex) => (
                            <div
                                key={`seat-${rowIndex}-${seatIndex}`}
                                style={element ? seatStyle : spaceStyle}
                            />
                        ))}
                    </div>
                ))}
            </div>
            <div id="screen" style={screenStyle}>
                Screen
            </div>
        </div>
    );
};

export default CinemaHall;
