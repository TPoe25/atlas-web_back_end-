import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const rooms = [
    new ClassRoom(1),
    new ClassRoom(2),
    new ClassRoom(5),
  ];

  console.log('[]');
  return rooms.map((room) => room._maxStudentsSize);
}
