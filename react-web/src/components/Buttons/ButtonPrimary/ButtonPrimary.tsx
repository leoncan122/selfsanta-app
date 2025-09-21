import { ReactElement } from 'react';
import './ButtonPrimary.css';

interface ButtonPrimaryProps {
    children: ReactElement | string;
    onClick?: () => void;
    type?: "button" | "submit" | "reset" | undefined;
    disabled?: boolean;
}
export const ButtonPrimary = ({
    children,
    onClick,
    type = "button",
    disabled = false,
}: ButtonPrimaryProps) : ReactElement => {
    return (    
        <button
            className="btn-primary"
            onClick={onClick}
            type={type}
            disabled={disabled}
        >   {children}
        </button>
    );  
};

export default ButtonPrimary;