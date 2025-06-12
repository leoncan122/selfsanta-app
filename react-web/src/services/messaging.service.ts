import { Message } from "../mocks/messages";


class MessagingService {
  private static instance: MessagingService;
  socket: WebSocket | null = null;
  private listeners: Array<(message: Message) => void> = [];

  constructor() {}

  public static getInstance(): MessagingService {
    if (!MessagingService.instance) {
      MessagingService.instance = new MessagingService();
    }
    return MessagingService.instance;
  }

  public connect(url: string): void {
    if (this.socket) {
      this.socket.close();
    }
    this.socket = new WebSocket(url);
  }

  public sendMessage(message: Message): void {
    if (this.socket && this.socket.readyState === WebSocket.OPEN) {
      this.socket.send(JSON.stringify(message));
    } else {
      console.error("WebSocket is not open.");
    }
  }

  public onMessage(callback: (message: Message) => void): void {
    this.listeners.push(callback);
    if (this.socket) {
      this.socket.onmessage = (event) => {
        try {
          const msg = JSON.parse(JSON.parse(event.data));
          // console.log("Received message:",  msg);

          this.listeners.forEach(callback => callback(msg));
        } catch (e) {
          console.error("Error parsing message", e);
        }
      };
    }
  }
};


export const messagingService = MessagingService.getInstance();
export const connectToMessagingService = (url: string): void => {
  messagingService.connect(url);
}