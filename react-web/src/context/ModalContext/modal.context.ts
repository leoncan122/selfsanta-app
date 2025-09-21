import { createContext, useEffect } from "react";
import { useContext } from "react";


interface ModalContext {
    isModalOpen: boolean;
    setIsModalOpen: (isModalOpen: boolean) => void;
}

export const initialState: ModalContext = {
    isModalOpen: false,
    setIsModalOpen: () => {}
}


export const ModalContext = createContext(initialState); 

export const useModalContext = (isOpen?: boolean ) => {
    const context = useContext<ModalContext>(ModalContext);

    useEffect(() => {
        if (isOpen !== undefined) {
            context.setIsModalOpen(isOpen);
        }
    }, [isOpen]);

    if (context === undefined) {
        throw new Error('useModalContext must be used within a ModalProvider');
    }

    return context;
}   