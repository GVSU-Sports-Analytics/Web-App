import Image from "next/image";


export default function HeaderImage() {
    return (
        <Image 
        src="/../public/louie.gif"
        alt="louie-bg"
        width={700}
        height={700}
        className="w-full"
        >
        </Image>
    )
}
