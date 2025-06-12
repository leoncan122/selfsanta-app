export interface SendMessageButtonProps {
    threadId: string;
    onSendMessage: (threadId: string, message: string) => void;
}