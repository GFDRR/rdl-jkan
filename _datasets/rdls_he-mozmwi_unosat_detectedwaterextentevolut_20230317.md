---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-and-evolution-over-southern-region-in-malawi-tete-and-zambezia-provinces-in-m
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNOSAT Population Exposure Assessment
    url: https://data.humdata.org/dataset/water-extent-and-evolution-over-southern-region-in-malawi-tete-and-zambezia-provinces-in-m
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-and-evolution-over-southern-region-in-malawi-tete-and-zambezia-provinces-in-m
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-and-evolution-over-southern-region-in-malawi-tete-and-zambezia-provinces-in-m
dataset_id: rdls_he-mozmwi_unosat_detectedwaterextentevolut_20230317
description: "UNOSAT code TC20230314MWI, GDACS Id: 1000961 This map illustrates satellite-detected\
  \ surface waters in Southern Region, Malawi & Tete and Zambezia Provinces, Mozambique\
  \ as observed from a Sentinel-1 image acquired on 17 Mar. 2023 at 05:09 local time.\
  \ Within the analyzed area in Malawi of about 5,000 km2, about 320 km2 of land appear\
  \ to be flooded. Water extent appears to have increased of about 60km\xB2 since\
  \ the 14 Mar. 2023. Within the analyzed area in Mozambique of about 20,500 km2,\
  \ about 1,000 km2 of land appear to be flooded. Water extent appears to have increased\
  \ of about 150km\xB2 since the 14 Mar. 2023. Based on Worldpop population data and\
  \ the detected surface waters in the analyzed area in Malawi and Mozambique, respectively\
  \ ~47,000 people and ~75,000 people are potentially exposed or living close to flooded\
  \ areas. This is a preliminary analysis and has not yet been validated in the field.\
  \ Please send ground feedback to United Nations Satellite Centre (UNOSAT). Important\
  \ note: Flood analysis from radar images may underestimate the presence of standing\
  \ waters in built-up areas and densely vegetated areas due to the backscattering\
  \ properties of the radar signal.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-and-evolution-over-southern-region-in-malawi-tete-and-zambezia-provinces-in-m]"
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
    description: Population exposed to detected flood extent in Southern Malawi and
      Tete/Zambezia Mozambique
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Sentinel-1 SAR satellite imagery acquired on 14 and 17 March 2023\
    \ was analyzed by UNOSAT analysts to detect surface water extent through image\
    \ comparison and change detection. Water-covered areas were mapped and quantified\
    \ (320 km\xB2 in Malawi, 1,000 km\xB2 in Mozambique), with area changes calculated\
    \ between acquisition dates. Population exposure was subsequently assessed against\
    \ the detected flood extent."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: UNOSAT Population Exposure Assessment
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-and-evolution-over-southern-region-in-malawi-tete-and-zambezia-provinces-in-m
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
  description: Satellite detected water extent and evolution over Southern Region
    in Malawi & Tete and Zambezia Provinces in Mozambique between 14 and 17 March
    2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3536/TC20230314MWI_gdb.zip
  format: Geodatabase
  id: resource_a91bb2a3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230314MWI_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent and evolution over Southern Region
    in Malawi & Tete and Zambezia Provinces in Mozambique between 14 and 17 March
    2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3536/TC20230314MWI_SHP.zip
  format: null
  id: resource_fdd00b65
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230314MWI_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent and evolution over Southern Region
    in Malawi & Tete and Zambezia Provinces in Mozambique between 14 and 17 March
    2023 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3536/UNOSAT_Population_Exposure_TC20230314MWI_SouthernRegion_Malawi_17Mar2023.xlsx
  format: null
  id: resource_a1f5b380
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_TC20230314MWI_SouthernRegion_Malawi_17Mar2023.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-mozmwi_unosat_detectedwaterextentevolut_20230317
spatial:
  bbox: null
  centroid: null
  countries:
  - MWI
  - MOZ
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-03-17'
temporal_resolution: null
title: Satellite detected water extent and evolution over Southern Region in Malawi
  & Tete and Zambezia Provinces in Mozambique between 14 and 17 March 2023
version: null
vulnerability: null
---
