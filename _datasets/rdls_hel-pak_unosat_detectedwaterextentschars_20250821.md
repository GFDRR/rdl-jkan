---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/water-extents-in-charsadda-nowshera-and-peshawar-districts-khyber-pakhtunkhwa-province-pak
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extents-in-charsadda-nowshera-and-peshawar-districts-khyber-pakhtunkhwa-province-pak
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-charsadda-nowshera-and-peshawar-districts-khyber-pakhtunkhwa-province-pak
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-charsadda-nowshera-and-peshawar-districts-khyber-pakhtunkhwa-province-pak
dataset_id: rdls_hel-pak_unosat_detectedwaterextentschars_20250821
description: "UNOSAT code: FL20250818PAK This map illustrates the satellite detected\
  \ water extent in Charsadda, Nowshera and Peshawar Districts, Khyber Pakhtunkhwa\
  \ Province, Pakistan as observed from a Sentinel-2 satellite image acquired on 20\
  \ August 2025 at 13:35 local time (08:35 UTC). Within the analyzed area of approximately\
  \ 1,800 km\xB2, about 35 km\xB2 of land appears to be affected by floodwaters. The\
  \ floodwater extent appears to have receded by approximately 20 km\xB2 since 16\
  \ August 2025. Based on WorldPop population data and the flood extent, approximately\
  \ 41,000 people are potentially exposed or living close to the flooded areas. This\
  \ is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-in-charsadda-nowshera-and-peshawar-districts-khyber-pakhtunkhwa-province-pak]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Residential population potentially exposed to floodwaters based on
      WorldPop data overlay with observed flood extent
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
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
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts visually interpreted Sentinel-2 satellite imagery\
    \ acquired on 20 August 2025 to delineate water extent polygons in three districts\
    \ of Khyber Pakhtunkhwa Province. The observed flood extent (35 km\xB2) was spatially\
    \ intersected with WorldPop gridded population data to estimate approximately\
    \ 41,000 potentially affected people. Temporal comparison with imagery from 16\
    \ August 2025 indicated a 20 km\xB2 recession in floodwater extent."
  sources:
  - id: source_1
    license: null
    name: Sentinel-2 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-in-charsadda-nowshera-and-peshawar-districts-khyber-pakhtunkhwa-province-pak
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially affected by observed floodwaters in Charsadda,
      Nowshera and Peshawar Districts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  description: Satellite detected water extents in Charsadda, Nowshera and Peshawar
    Districts, Khyber Pakhtunkhwa Province, Pakistan as of 20 August 2025 (Zipped
    geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4175/FL20250818PAK_gdb.zip
  format: Geodatabase
  id: resource_2d1ee2f9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250818PAK_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Charsadda, Nowshera and Peshawar
    Districts, Khyber Pakhtunkhwa Province, Pakistan as of 20 August 2025 (Zipped
    shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4175/FL20250818PAK_SHP.zip
  format: null
  id: resource_92c1545e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250818PAK_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Charsadda, Nowshera and Peshawar
    Districts, Khyber Pakhtunkhwa Province, Pakistan as of 20 August 2025 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4175/PopulationExposure_FL20250818PAK_PK_Province.xlsx
  format: null
  id: resource_c33e652f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PopulationExposure_FL20250818PAK_PK_Province.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-pak_unosat_detectedwaterextentschars_20250821
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-08-21'
temporal_resolution: null
title: Satellite detected water extents in Charsadda, Nowshera and Peshawar Districts,
  Khyber Pakhtunkhwa Province, Pakistan as of 20 August 2025
version: null
vulnerability: null
---
