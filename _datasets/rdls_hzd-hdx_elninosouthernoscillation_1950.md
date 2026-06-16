---
attributions:
- entity:
    affiliation: null
    email: null
    name: National Oceanic and Atmospheric Administration (NOAA) Climate Prediction
      Center (CPC)
    url: https://data.humdata.org/dataset/el-nino-southern-oscillation-enso-el-nino-and-la-nina-events
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/el-nino-southern-oscillation-enso-el-nino-and-la-nina-events
creator:
  affiliation: null
  email: null
  name: National Oceanic and Atmospheric Administration (enso) / Climate Prediction
    Center (CPC)
  url: https://data.humdata.org/dataset/el-nino-southern-oscillation-enso-el-nino-and-la-nina-events
dataset_id: rdls_hzd-hdx_elninosouthernoscillation_1950
description: "ENSO stands for El Ni\xF1o/ Southern Oscillation. The ENSO cycle refers\
  \ to the coherent and sometimes very strong year-to-year variations in sea- surface\
  \ temperatures, convective rainfall, surface air pressure, and atmospheric circulation\
  \ that occur across the equatorial Pacific Ocean. El Ni\xF1o and La Ni\xF1a represent\
  \ opposite extremes in the ENSO cycle. El Ni\xF1o refers to the above-average sea-surface\
  \ temperatures that periodically develop across the east-central equatorial Pacific.\
  \ It represents the warm phase of the ENSO cycle, and is sometimes referred to as\
  \ a Pacific warm episode. La Ni\xF1a refers to the periodic cooling of sea-surface\
  \ temperatures across the east-central equatorial Pacific. It represents the cold\
  \ phase of the ENSO cycle, and is sometimes referred to as a Pacific cold episode.\
  \ View the raw data View the processed data Dataset field definitions: date: Year-month-date\
  \ (first day of month) TOTAL: ERSST.v5 (sea surface temperature) in the Ni\xF1o\
  \ 3.4 region ClimAdjust: adjustment for changing 30-year base period ANOM: Oceanic\
  \ Ni\xF1o Index (ONI) ANOM_trimester: 3-month rolling mean of ANOM (MO corresponds\
  \ to first month of trimester) ANOM_trimester_round: ANOM_trimester rounded to one\
  \ decimal place phase_trimester: phase of trimester based on ANOM_trimester_round\
  \ phase_event: elnino or lanina event (requiring at least 5 consecutive trimesters\
  \ of the phase). [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/el-nino-southern-oscillation-enso-el-nino-and-la-nina-events]"
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    drought:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: SPI:-
        process: meteorological_drought
        trigger: null
        type: drought
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "ENSO phase data derived from observed sea-surface temperature anomalies\
    \ in the equatorial Pacific, processed by NOAA CPC using the Ocean Ni\xF1o Index\
    \ (ONI) methodology to classify warm (El Ni\xF1o) and cold (La Ni\xF1a) episodes\
    \ with trimester-level temporal resolution"
  sources:
  - id: source_1
    license: null
    name: National Oceanic and Atmospheric Administration (NOAA) Climate Prediction
      Center (CPC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/el-nino-southern-oscillation-enso-el-nino-and-la-nina-events
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: "[ENSO FAQ]((see referenced_by)) [Description of Changes to Ocean Ni\xF1\
  o Index (ONI)]((see referenced_by))"
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://www.cpc.ncep.enso.gov/products/analysis_monitoring/ensostuff/ensofaq.shtml#ENSO
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://www.cpc.ncep.enso.gov/products/analysis_monitoring/ensostuff/ONI_change.shtml
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "El Ni\xF1o-Southern Oscillation (ENSO): El Ni\xF1o and La Ni\xF1a\
    \ Events (Monthly analysis of the El Ni\xF1o-Southern Oscillation (ENSO) cycle)"
  download_url: https://data.humdata.org/dataset/82255636-d023-4351-95f6-95784cb8ceec/resource/2b97dd0a-2592-4c7e-8abd-6cbbcdf2f4b7/download/el-nino-southern-oscillation-enso-el-nino-and-la-nina-events.csv
  format: null
  id: resource_2b97dd0a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: el-nino-southern-oscillation-enso-el-nino-and-la-nina-events.csv
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-hdx_elninosouthernoscillation_1950
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-01'
  start: '1950-01-01'
temporal_resolution: null
title: "El Ni\xF1o-Southern Oscillation (ENSO): El Ni\xF1o and La Ni\xF1a Events"
version: null
vulnerability: null
---
