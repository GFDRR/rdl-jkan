---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/waters-evolution-over-khersonska-dnipropetrovska-mykolaivska-odeska-and-zaporizka-oblasts-
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-evolution-over-khersonska-dnipropetrovska-mykolaivska-odeska-and-zaporizka-oblasts-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-evolution-over-khersonska-dnipropetrovska-mykolaivska-odeska-and-zaporizka-oblasts-
dataset_id: rdls_hzd-ukr_unosat_detectedwatersevolutionov_20230720
description: "UNOSAT code FL20230606UKR This map illustrates satellite-detected water\
  \ using Sentinel-2 image acquired on the 15th of July 2023 and compared with the\
  \ water extent between the 03rd and the 05th of July 2023 after the Nova Kakhovka\
  \ dam wall break of the 06th of June 2023. Within the analysed area of 25,000 km\xB2\
  , surface waters appear to have receded by about 100 km\xB2 in cloud free zone since\
  \ the 5th of July 2023. No major changes observed in water level of the cooling\
  \ pond of the Zaporizhia nuclear power plant as of 15 July 2023 compared to 5 July\
  \ 2023. This is a preliminary analysis and has not yet been validated in the field.\
  \ Please send ground feedback to the United Nations Satellite Centre (UNOSAT)..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/waters-evolution-over-khersonska-dnipropetrovska-mykolaivska-odeska-and-zaporizka-oblasts-]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Sentinel-2 satellite imagery acquired on 15 July 2023 was compared\
    \ with baseline imagery from 3-5 July 2023 by UNOSAT analysts to detect changes\
    \ in surface water extent across 25,000 km\xB2 in five Ukrainian oblasts following\
    \ the Nova Kakhovka dam breach. Multi-temporal image analysis identified water\
    \ recession of approximately 100 km\xB2 in cloud-free zones."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/waters-evolution-over-khersonska-dnipropetrovska-mykolaivska-odeska-and-zaporizka-oblasts-
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Detected Waters Evolution over Khersonska, Dnipropetrovska,
    Mykolaivska,Odeska and Zaporizka Oblasts in Ukraine as of 15 July 2023 (Zipped
    geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3637/FL20230606UKR_gdb.zip
  format: Geodatabase
  id: resource_3c4c8d12
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230606UKR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Detected Waters Evolution over Khersonska, Dnipropetrovska,
    Mykolaivska,Odeska and Zaporizka Oblasts in Ukraine as of 15 July 2023 (Zipped
    shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3637/FL20230606UKR_SHP.zip
  format: null
  id: resource_26ff6a95
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230606UKR_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ukr_unosat_detectedwatersevolutionov_20230720
spatial:
  bbox: null
  centroid: null
  countries:
  - UKR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-07-20'
temporal_resolution: null
title: Satellite Detected Waters Evolution over Khersonska, Dnipropetrovska, Mykolaivska,Odeska
  and Zaporizka Oblasts in Ukraine as of 15 July 2023
version: null
vulnerability: null
---
