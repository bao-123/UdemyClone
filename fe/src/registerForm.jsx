import { useState } from "react";

function RegisterForm() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [email, setEmail] = useState("");

    return (
        <form>
            <div>
                <input type="text" placeholder="Username" onChange={e => setUsername(e.target.value)} />
            </div>
            <div>
                <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)}/>
            </div>
            <div>
                <input type="email" placeholder="Email" onChange={e => setEmail(e.target.value)}/>
            </div>
            <button type="submit">Register</button>
        </form>
    );
}

export default RegisterForm;