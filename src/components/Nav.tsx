import NavItem from "./NavItem"
import Link from 'next/link'

const linkStyle = "block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-white dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700"

const navLinks = [
    <Link href={"/"} className={linkStyle}>Home</Link>,
    <Link href={"/sports/baseball"} className={linkStyle}>Baseball</Link>,
    <Link href={"/sports/softball"} className={linkStyle}>Softball</Link>,
]


export default function Nav() {
    return (
        <div>
            <nav className="fixed z-10 bg-white px-2 sm:px-4 py-4 sm:py-2.5 dark:bg-gray-900 w-full top-0 left-0 border-b border-gray-200 dark:border-gray-600">
                    <div className="items-center justify-between hidden w-full md:flex md:w-auto md:order-1" id="navbar-sticky">
                        <ul className="flex flex-col p-4 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
                            {navLinks.map((item, index) => {
                                return (
                                    <NavItem 
                                    link={item}
                                    key={index}
                                    className="flex items-center"/>
                                )
                            })}
                        </ul>
                    </div>
            </nav>
        </div>
    )
}
