import { InputError, InputField, InputHeader, InputHighLight, InputLabel, InputWrapper } from "./input.styles";

interface InputProps {
  label: string;
  value: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  error: string;
}

export default function Input({ label, value, onChange, error }: InputProps) {
  return (
    <InputWrapper>
        <InputHeader>
            <InputLabel>{label}</InputLabel>
            {error ? (
                <InputError>{error}</InputError>
            ) :
                <InputHighLight>{value ? "OK" : "..."}</InputHighLight>
            }
        </InputHeader>
        <InputField
            value={value}
            onChange={onChange}
        />
    </InputWrapper>
  )
}