"""
Unit tests for program_functions.py
Tests core Biopython (FASTA parsing), file handling, and data processing functions.
"""

import pytest
import pandas as pd
import tempfile
import os
from pathlib import Path
from program_functions import fasta_to_dict, fasta_file_path, adjust_csv


class TestFastaToDict:
    """Test FASTA parsing with Biopython (SeqIO)"""
    
    def test_fasta_parsing_single_sequence(self, tmp_path):
        """Test parsing a single FASTA sequence"""
        fasta_file = tmp_path / "test.fasta"
        fasta_file.write_text(">seq1\nATGCATGC\n")
        
        result = fasta_to_dict(str(fasta_file))
        assert "seq1" in result
        assert str(result["seq1"]) == "ATGCATGC"
    
    def test_fasta_parsing_multiple_sequences(self, tmp_path):
        """Test parsing multiple FASTA sequences (pathogen genes)"""
        fasta_file = tmp_path / "genes.fasta"
        fasta_file.write_text(">holY\nMARTNGLEVALFEAR\n>elyY\nMKLVFLGVALLLCSLSVA\n")
        
        result = fasta_to_dict(str(fasta_file))
        assert len(result) == 2
        assert "holY" in result
        assert "elyY" in result
    
    def test_fasta_returns_dict(self, tmp_path):
        """Test that FASTA parsing returns a dictionary"""
        fasta_file = tmp_path / "test.fasta"
        fasta_file.write_text(">seq1\nATGC\n")
        
        result = fasta_to_dict(str(fasta_file))
        assert isinstance(result, dict)


class TestFastaFileValidation:
    """Test FASTA file existence and validation"""
    
    def test_valid_fasta_file_exists(self, tmp_path):
        """Test that valid file path passes validation"""
        fasta_file = tmp_path / "valid.fasta"
        fasta_file.write_text(">seq1\nATGC\n")
        
        result = fasta_file_path(str(fasta_file))
        assert result == str(fasta_file)
    
    def test_nonexistent_file_raises_error(self, tmp_path):
        """Test that missing file raises FileNotFoundError"""
        nonexistent = tmp_path / "missing.fasta"
        
        with pytest.raises(FileNotFoundError):
            fasta_file_path(str(nonexistent))


class TestCsvProcessing:
    """Test CSV adjustment function (BLAST result formatting)"""
    
    def test_csv_headers_applied(self, tmp_path):
        """Test that headers are correctly added to BLAST CSV"""
        csv_file = tmp_path / "blast_results.csv"
        csv_file.write_text(
            "CAI77377.1,hoiY,100,50,0,1,50,1e-30\n"
            "CAI77378.1,elyY,98,50,1,1,50,1e-28\n"
        )
        
        df = adjust_csv(str(csv_file))
        expected_headers = ["Protein ID", "Sequence ID", "% Identity", "Alignment Length", 
                           "Mismatches", "Query Start", "Query End", "E-Value"]
        assert list(df.columns) == expected_headers
        assert len(df) == 2
    
    def test_csv_data_preserved(self, tmp_path):
        """Test that CSV data is preserved after adding headers"""
        csv_file = tmp_path / "blast_results.csv"
        csv_file.write_text("CAI77377.1,holY,100,50,0,1,50,1e-30\n")
        
        df = adjust_csv(str(csv_file))
        assert df.iloc[0]["Protein ID"] == "CAI77377.1"
        assert df.iloc[0]["Sequence ID"] == "holY"
        assert df.iloc[0]["% Identity"] == 100


class TestSequenceRetrieval:
    """Test sequence lookup functionality"""
    
    def test_retrieve_sequence_by_id(self, tmp_path):
        """Test retrieving sequence by ID from parsed FASTA"""
        fasta_file = tmp_path / "genes.fasta"
        fasta_file.write_text(">holY\nMARTNGLEVALFEAR\n>yRz1\nMSKFLTALISFLFSSLLSAC\n")
        
        sequences = fasta_to_dict(str(fasta_file))
        assert "holY" in sequences
        assert str(sequences["holY"]) == "MARTNGLEVALFEAR"
    
    def test_sequence_lookup_case_sensitive(self, tmp_path):
        """Test that ID lookup respects case sensitivity"""
        fasta_file = tmp_path / "genes.fasta"
        fasta_file.write_text(">yRz1\nMSKFLTALISFLFSSLLSAC\n")
        
        sequences = fasta_to_dict(str(fasta_file))
        assert "yRz1" in sequences
        assert "YRZ1" not in sequences
