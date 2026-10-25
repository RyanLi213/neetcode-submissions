class Solution:

    def encode(self, strs: List[str]) -> str:
        combined_str = False
        if len(strs)== 0:
            combined_str = "True"
            return combined_str
        combined_str = "asjdi".join(strs)
        return combined_str

    def decode(self, s: str) -> List[str]:
        if s == "True":
            return []
        return s.split("asjdi")