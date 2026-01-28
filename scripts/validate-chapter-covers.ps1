# ========== CHAPTER COVER VALIDATION SCRIPT ==========
# Validates that all chapter covers follow the established pattern
# Property 8: Chapter Cover Consistency

Write-Host "========== SYMPHONY BOOK: CHAPTER COVER VALIDATION ==========" -ForegroundColor Cyan
Write-Host ""

$totalChapters = 26
$validationResults = @()
$allValid = $true

Write-Host "Validating chapter covers for consistency..." -ForegroundColor Yellow
Write-Host ""

for ($i = 1; $i -le $totalChapters; $i++) {
    $chapterPath = "content/chapter$i"
    $coverPath = "$chapterPath/chapter_cover.tex"
    
    Write-Host "Chapter $i : " -NoNewline
    
    if (Test-Path $coverPath) {
        Write-Host "FOUND" -ForegroundColor Green -NoNewline
        
        # Read the cover file content
        $content = Get-Content $coverPath -Raw
        
        # Check for required pattern elements
        $patternChecks = @()
        
        # Check for TikZ graphics (chapter number shape)
        if ($content -match "\\begin\{tikzpicture\}") {
            $patternChecks += "TikZ-OK"
        } else {
            $patternChecks += "TikZ-MISSING"
            $allValid = $false
        }
        
        # Check for chapter topic typography
        if ($content -match "fontsize.*textcolor.*textit") {
            $patternChecks += "Typography-OK"
        } else {
            $patternChecks += "Typography-MISSING"
            $allValid = $false
        }
        
        # Check for separator (look for rule pattern)
        if ($content -match "\\rule\{.*\}\{.*pt\}") {
            $patternChecks += "Separator-OK"
        } else {
            $patternChecks += "Separator-MISSING"
            $allValid = $false
        }
        
        # Check for tcolorbox
        if ($content -match "\\begin\{tcolorbox\}") {
            $patternChecks += "ContentBox-OK"
        } else {
            $patternChecks += "ContentBox-MISSING"
            $allValid = $false
        }
        
        # Check for brand colors
        if ($content -match "brandPrimary|brandSecondary|brandAccent") {
            $patternChecks += "BrandColors-OK"
        } else {
            $patternChecks += "BrandColors-MISSING"
            $allValid = $false
        }
        
        # Check for clearpage
        if ($content -match "\\clearpage") {
            $patternChecks += "PageBreak-OK"
        } else {
            $patternChecks += "PageBreak-MISSING"
            $allValid = $false
        }
        
        Write-Host " | " -NoNewline
        Write-Host ($patternChecks -join " | ")
        
        $validationResults += [PSCustomObject]@{
            Chapter = $i
            HasCover = $true
            PatternElements = $patternChecks
            Valid = ($patternChecks -notlike "*MISSING*")
        }
        
    } else {
        Write-Host "MISSING COVER FILE" -ForegroundColor Red
        $allValid = $false
        
        $validationResults += [PSCustomObject]@{
            Chapter = $i
            HasCover = $false
            PatternElements = @("File-MISSING")
            Valid = $false
        }
    }
}

Write-Host ""
Write-Host "========== VALIDATION SUMMARY ==========" -ForegroundColor Cyan

$coversFound = ($validationResults | Where-Object { $_.HasCover }).Count
$validCovers = ($validationResults | Where-Object { $_.Valid }).Count

Write-Host "Total Chapters: $totalChapters"
Write-Host "Covers Found: $coversFound/$totalChapters" -ForegroundColor $(if ($coversFound -eq $totalChapters) { "Green" } else { "Yellow" })
Write-Host "Valid Covers: $validCovers/$totalChapters" -ForegroundColor $(if ($validCovers -eq $totalChapters) { "Green" } else { "Yellow" })

if ($allValid) {
    Write-Host ""
    Write-Host "ALL CHAPTER COVERS PASS VALIDATION" -ForegroundColor Green
    Write-Host "Property 8: Chapter Cover Consistency - VALIDATED" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "SOME CHAPTER COVERS NEED ATTENTION" -ForegroundColor Yellow
    Write-Host "Property 8: Chapter Cover Consistency - NEEDS REVIEW" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========== PATTERN REQUIREMENTS ==========" -ForegroundColor Cyan
Write-Host "Each chapter cover should include:"
Write-Host "1. Big chapter number in content-reflective TikZ shape"
Write-Host "2. Chapter topic with elegant typography (28pt italic)"
Write-Host "3. Nice separator with decorative elements"
Write-Host "4. This chapter explores content box with 6 bullet points"
Write-Host "5. Proper brand color usage (brandPrimary, brandSecondary, brandAccent)"
Write-Host "6. Single page format with clearpage"

Write-Host ""
Write-Host "Validation complete." -ForegroundColor Cyan