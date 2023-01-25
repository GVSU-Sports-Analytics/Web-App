

export default function NavItem(props) {
    return (
        <li>
            <a 
            className="block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-white dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700"
            href={props.props.href}>
            {props.props.text}
            </a>
        </li>
    )
}