import { ButtonWrapper } from "./button.styles";

interface ButtonProps {
  children: React.ReactNode;
  onClick: () => void;
}

export default function Button({ children, onClick }: ButtonProps) {
  return (
    <ButtonWrapper onClick={onClick}>
        {children}
    </ButtonWrapper>
  )
}