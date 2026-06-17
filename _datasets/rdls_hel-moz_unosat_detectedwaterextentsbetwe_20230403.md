---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-27-and-31-march-2023-over-mozambique
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-27-and-31-march-2023-over-mozambique
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-27-and-31-march-2023-over-mozambique
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-27-and-31-march-2023-over-mozambique
dataset_id: rdls_hel-moz_unosat_detectedwaterextentsbetwe_20230403
description: "UNOSAT code TC20230221MOZ, GDACS Id: 1000961 This map illustrates cumulative\
  \ satellite-detected water using VIIRS in Mozambique between 27 to 31 March 2023.\
  \ Within the cloud-free analyzed areas of about 600,000 km\xB2, a total of about\
  \ 12,000 km\xB2 of land appear to be affected by flood waters. Water extent appears\
  \ to have decreased by about 6,300 km2 since 21-25 March 2023. Based on Worldpop\
  \ population data and the maximal flood water extent, ~650,000 people are potentially\
  \ exposed or living close to flooded areas mainly located in Zambezia province with\
  \ ~220,000 people and Sofala province with ~140,000 people. This preliminary analysis\
  \ has not yet been validated in the field. Please send ground feedback to the United\
  \ Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-between-27-and-31-march-2023-over-mozambique]"
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
    description: Population potentially exposed or living close to flooded areas,
      derived from WorldPop data intersected with maximal flood water extent
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts processed VIIRS satellite imagery from 27-31 March
    2023 over Mozambique, comparing multi-temporal images to detect cumulative water
    extent changes and identify flooded areas. WorldPop population data was intersected
    with the maximal flood water extent to estimate population exposure. The resulting
    dataset provides observed flood inundation area and affected population counts
    for the cyclone-induced flooding event.
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
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-between-27-and-31-march-2023-over-mozambique
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood waters detected via satellite imagery
      during the 27-31 March 2023 event
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
  description: Satellite detected water extents between 27 and 31 March 2023 over
    Mozambique (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3554/TC20230221MOZ.gdb.zip
  format: Geodatabase
  id: resource_950be8d3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230221MOZ.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 27 and 31 March 2023 over
    Mozambique (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3554/TC20230221MOZ_shp.zip
  format: null
  id: resource_f10f9c82
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230221MOZ_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 27 and 31 March 2023 over
    Mozambique (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3554/UNOSAT_Population_Exposure_TC20230221MOZ_27Mar_31Mar2023_Mozambique.xlsx
  format: null
  id: resource_9be1bb8b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_TC20230221MOZ_27Mar_31Mar2023_Mozambique.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-moz_unosat_detectedwaterextentsbetwe_20230403
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-04-03'
temporal_resolution: null
title: Satellite detected water extents between 27 and 31 March 2023 over Mozambique
version: null
vulnerability: null
---
