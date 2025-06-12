export interface MessagesListItemProps {
    key: number | string;
    children: React.ReactNode;
}

export const MessagesListItem = ({ key, children }: MessagesListItemProps) => {
    return (
        <li key={key} className="messages-item">
            {children}
        </li>
    );
};