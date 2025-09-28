def validate_chain_integrity(chain):
    """
    Blok zincirinin bütünlüğünü kontrol eder.
    """
    for i in range(1, len(chain)):
        current_block = chain[i]
        previous_block = chain[i-1]
        
        # Mevcut bloğun "previous_hash" alanı, bir önceki bloğun "hash" alanına eşit mi?
        if current_block['previous_hash'] != previous_block['hash']:
            print(f"Bütünlük bozuldu! Blok {i} geçersiz.")
            return False
            
    print("Zincir bütünlüğü doğrulandı. Hiçbir sorun yok.")
    return True

if __name__ == "__main__":
    # Basit bir blok zinciri simülasyonu (sözlük listesi olarak)
    blockchain = [
        {'hash': 'hash_0', 'previous_hash': '0'},
        {'hash': 'hash_1', 'previous_hash': 'hash_0'},
        {'hash': 'hash_2', 'previous_hash': 'hash_1'},
    ]
    
    print("--- Geçerli Zincir Testi ---")
    validate_chain_integrity(blockchain)

    # Zinciri bozalım
    broken_blockchain = [
        {'hash': 'hash_0', 'previous_hash': '0'},
        {'hash': 'hash_1', 'previous_hash': 'hash_0'},
        {'hash': 'hash_2_bozuk', 'previous_hash': 'YANLIS_HASH'}, # Hatalı bağlantı
    ]

    print("\n--- Bozuk Zincir Testi ---")
    validate_chain_integrity(broken_blockchain)