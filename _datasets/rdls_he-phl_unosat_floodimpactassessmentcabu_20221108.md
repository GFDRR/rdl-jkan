---
attributions:
- entity:
    affiliation: null
    email: null
    name: Worldpop
    url: https://data.humdata.org/dataset/flood-impact-assessment-of-cabuyao-city-and-city-of-calamba-laguna-province-region-iv-a-ph
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Kanopus-V satellite imagery
    url: https://data.humdata.org/dataset/flood-impact-assessment-of-cabuyao-city-and-city-of-calamba-laguna-province-region-iv-a-ph
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-of-cabuyao-city-and-city-of-calamba-laguna-province-region-iv-a-ph
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-of-cabuyao-city-and-city-of-calamba-laguna-province-region-iv-a-ph
dataset_id: rdls_he-phl_unosat_floodimpactassessmentcabu_20221108
description: 'UNOSAT code TC20221028PHL, GDACS Id: 1000942 This map illustrates satellite-detected
  surface waters in Cabuyao City and City of Calamba, Laguna Province, Region IV-A,
  Philippines as observed from a Kanopus-V image acquired 5 November 2022 at 11:12
  local time. Within the analysis extent of about 2,200 hectares, approximately 120
  hectares of land appear to be flooded. Based on Worldpop population data and the
  detected surface waters within the analysis extent, approximately 4,400 people are
  potentially exposed to or living close to flooded areas along with 256 structures
  and a port potentially affected by flooding. This is a preliminary analysis and
  has not yet been validated in the field. Please send ground feedback to United Nations
  Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/flood-impact-assessment-of-cabuyao-city-and-city-of-calamba-laguna-province-region-iv-a-ph]'
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
    description: Population potentially exposed to or living close to flooded areas
      based on WorldPop data
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
- asset_type:
    description: Building structures identified within the flooded extent
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
  metrics:
  - dimension: structure
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
license: CC-BY-SA-4.0
lineage:
  description: Satellite imagery from Kanopus-V acquired on 5 November 2022 was analyzed
    by UNOSAT to detect surface water extent through comparison with reference imagery.
    Detected flooded areas (approximately 120 hectares) were intersected with WorldPop
    gridded population data and building footprints to estimate exposure of approximately
    4,400 people and 256 structures to the observed flood event in the 2,200 hectare
    analysis extent.
  sources:
  - id: source_1
    license: null
    name: Worldpop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Kanopus-V satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/flood-impact-assessment-of-cabuyao-city-and-city-of-calamba-laguna-province-region-iv-a-ph
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
  description: Flood Impact assessment of Cabuyao City and City of Calamba, Laguna
    Province, Region IV-A, Philippines as of 5 November 2022 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3441/TC20221028PHL_gdb.zip
  format: Geodatabase
  id: resource_e4de3511
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20221028PHL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood Impact assessment of Cabuyao City and City of Calamba, Laguna
    Province, Region IV-A, Philippines as of 5 November 2022 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3441/TC20221028PHL_SHP.zip
  format: null
  id: resource_80dd82c6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20221028PHL_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-phl_unosat_floodimpactassessmentcabu_20221108
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-11-08'
temporal_resolution: null
title: Flood Impact assessment of Cabuyao City and City of Calamba, Laguna Province,
  Region IV-A, Philippines as of 5 November 2022
version: null
vulnerability: null
---
