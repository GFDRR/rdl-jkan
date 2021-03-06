---
schema: rdl
title: Afghanistan Earthquake ground shaking hazard scenarios
organization: GFDRR
filename: hzd-afg-eq
resources:
  - name: Afghanistan Earthquake ground shaking hazard scenarios
    aggregation_type: Grid
    format:
      - geotiff
    h-res: 1 km
    epsg: 32642 (WGS84 UTM42N)
    url: >-
      https://development-data-hub-s3-public.s3.amazonaws.com/ddhfiles/1242186/hzd-afg-eq.zip
category:
  - Hazard
abstract: >-
  Earthquake hazard map representing Peak ground acceleration (PGA) measured in
  units of g for seven return period scenarios: RP10, RP50, RP100,
  RP250, RP500 , RP1000 and RP2500 years. 
notes: ''
source: AF-MHRA
model_date: '2016'
version: '1'
purpose: >-
  These maps have been derived on a nation-wide scale for the purpose of
  identifying high risk- areas on the district and provincial scale, from which
  decisions can be made on allocating efforts for more detailed site specific
  hazard and risk analysis. Use of this information on smaller scales should be
  applied with care. Importantly for on a local scale, it is often the case that
  more detailed case history and hazard information is required to perform such
  hazard and risk modelling, particularly where applied to dimension mitigation
  structures or strategies.
project: Afghanistan Multi-Hazard Risk Assessment (MHRA)
biblio_title: World Bank (2018) - Afghanistan Multi-Hazard Risk Assessment
biblio_url: 'https://www.gfdrr.org/sites/default/files/publication/Afghanistan_MHRA.pdf'
geo_coverage:
  - AFG
license: 'https://creativecommons.org/licenses/by/4.0/'
maintainer: GFDRR
maintainer_email: contact@riskdatalibrary.org
hazard_type:
  - EQ
analysis_type: Probabilistic
geo_area: ''
time_start: ''
time_end: ''
time_span: ''
time_year: ''
calculation_method: Simulated
frequency_type:
  - Return Period
return_period: '10, 50, 100, 250, 500, 1000, 2500 years'
occurrence_time_start: '800'
occurrence_time_end: '2001'
occurrence_time_span: '1200'
description: ''
process_type:
  - QGM
imt:
  - PGA_m/s2
data_uncertainty: ''
---
