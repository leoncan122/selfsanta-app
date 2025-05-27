import { ReactNode } from "react";



export interface FundsItemInfoProps {
    children: ReactNode;
}


const FundsItemInfo = ({ children }: FundsItemInfoProps) => {
    return (
        <div className="funds-info">
            {children}
        </div>
    )
}

export default FundsItemInfo;