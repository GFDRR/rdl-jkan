---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR imagery
    url: https://data.humdata.org/dataset/water-extent-in-manakara-atsimo-district-vatovavy-fitovinany-region-madagascar-as-of-05-ja
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extent-in-manakara-atsimo-district-vatovavy-fitovinany-region-madagascar-as-of-05-ja
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-manakara-atsimo-district-vatovavy-fitovinany-region-madagascar-as-of-05-ja
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-manakara-atsimo-district-vatovavy-fitovinany-region-madagascar-as-of-05-ja
dataset_id: rdls_hel-mdg_unosat_detectedwaterextentmanaka_20240108
description: "UNOSAT code: TC20240102MDG, GDACS ID: 1001040 This map illustrates satellite-detected\
  \ water extent in Manakara Atsimo District, Vatovavy Fitovinany Region as observed\
  \ from a Sentinel-1 image acquired on 05 January 2024 at 05:20 local time. Within\
  \ the extent of this map of about 300 km\xB2, a total of about 20 km\xB2 of lands\
  \ appear to be affected with flood waters. Based on Worldpop population data and\
  \ the detected surface waters, about 6,300 people are potentially exposed or living\
  \ close to flooded areas. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT). Important note: Flood analysis from radar images may underestimate the\
  \ presence of standing waters in built-up areas and densely vegetated areas due\
  \ to backscattering properties of the radar signal.. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/water-extent-in-manakara-atsimo-district-vatovavy-fitovinany-region-madagascar-as-of-05-ja]"
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
    description: Population potentially exposed or living close to flooded areas derived
      from WorldPop data
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
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Sentinel-1 SAR imagery acquired on 05 January 2024 was analyzed by\
    \ UNOSAT to detect surface water extent through comparison with reference imagery.\
    \ Detected water polygons (~20 km\xB2) were intersected with WorldPop gridded\
    \ population data to estimate approximately 6,300 people potentially exposed to\
    \ flooding in Manakara Atsimo District, Madagascar following a cyclone event."
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 SAR imagery
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
- href: https://data.humdata.org/dataset/water-extent-in-manakara-atsimo-district-vatovavy-fitovinany-region-madagascar-as-of-05-ja
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by detected flood waters in Manakara Atsimo District
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
  description: Satellite detected water extent in Manakara Atsimo District, Vatovavy
    Fitovinany Region, Madagascar as of 05 January 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3784/TC20240102MDG_gdb.zip
  format: Geodatabase
  id: resource_60305cd3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20240102MDG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Manakara Atsimo District, Vatovavy
    Fitovinany Region, Madagascar as of 05 January 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3784/TC20240102MDG_SHP.zip
  format: null
  id: resource_afa5e8c9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20240102MDG_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Manakara Atsimo District, Vatovavy
    Fitovinany Region, Madagascar as of 05 January 2024 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3784/UNOSAT_Population_Exposure_TC20240102MDG_ManakraAtsimo_VatovavtFitovinanyRegion_Madagascar_5Jan2024.xlsx
  format: null
  id: resource_3fa9f5f3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_TC20240102MDG_ManakraAtsimo_VatovavtFitovinanyRegion_Madagascar_5Jan2024.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mdg_unosat_detectedwaterextentmanaka_20240108
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-01-08'
temporal_resolution: null
title: Satellite detected water extent in Manakara Atsimo District, Vatovavy Fitovinany
  Region, Madagascar as of 05 January 2024
version: null
vulnerability: null
---
