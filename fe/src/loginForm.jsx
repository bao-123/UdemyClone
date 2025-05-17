import { useState } from 'react';

function LoginForm() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    return (
        <>
            <form
                id="loginForm"
                onSubmit={e => e.preventDefault()}
                className="flex flex-col bg-green-300 gap-y-[1.5em] items-center align-center px-[2rem] py-[4rem] mx-auto my-auto w-fit h-fit rounded-lg"
            >
                <h2 className="text-xl font-bold">Login</h2>
                <input
                    type="text"
                    value={username}
                    placeholder="Username"
                    autoComplete="off"
                    onChange={e => setUsername(e.target.value)}
                    className="bg-white p-2 rounded-xl border-gray-400 border focus:ring-1 focus:ring-green-500"
                />

                <input
                    type="password"
                    value={password}
                    placeholder="Password"
                    className="border border-gray-400 bg-white p-2 rounded-xl focus:ring-1 focus:ring-green-500"
                    onChange={e => setPassword(e.target.value)}
                />

                <input type="submit" className='bg-green-200 px-2 py-1 rounded-[8px] transition-all duration-500  hover:bg-green-500 hover:px-4 hover:py-2 ' value="Login" />
            </form>
        </>
    );
}

export default LoginForm;
