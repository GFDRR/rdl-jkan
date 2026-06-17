---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-waters-over-el-beni-department-bolivia
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-over-el-beni-department-bolivia
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-over-el-beni-department-bolivia
dataset_id: rdls_he-bol_unosat_detectedwatersoverelbenid_20180214
description: 'This map illustrates satellite-detected standing water over the El Beni
  department in Bolivia, as of the 12 February 2018, following heavy rainfalls that
  caused severe flooding in the area. The analysis was conducted using Radarsat-2
  image from 12 February 2018. UNITAR-UNOSAT identified in the analyzed area of the
  El Beni Department around 52,670 Ha of land that seem to be inundated, most of which
  are agricultural fields and swamps. The Rio Mamore has expanded along the banks.
  According to the analysis, the most affected province is Moxos, where more than
  35,500 Ha are submerged. In the municipality of Trinidad 6,900 Ha are detected as
  inundated. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/satellite-detected-waters-over-el-beni-department-bolivia]'
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
    description: Agricultural fields inundated by fluvial flooding in El Beni Department
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Swampland and riparian zones affected by river expansion and inundation
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
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
license: CC-BY-4.0
lineage:
  description: Radarsat-2 satellite imagery from 12 February 2018 was analyzed by
    UNOSAT analysts through visual interpretation and multi-temporal comparison to
    detect standing water and inundated areas. The analysis identified approximately
    52,670 hectares of inundated land, primarily agricultural fields and swamps, with
    spatial delineation provided as polygon vector data in shapefile format.
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
- href: https://data.humdata.org/dataset/satellite-detected-waters-over-el-beni-department-bolivia
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
  description: Satellite detected waters over El Beni department, Bolivia (zipped
    shapefile)
  download_url: https://cern.ch/unosat-maps/BO/FL20180209BOL/FL20180209BOL_shp.zip
  format: null
  id: resource_92907c45
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180209BOL_shp.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-bol_unosat_detectedwatersoverelbenid_20180214
spatial:
  bbox: null
  centroid: null
  countries:
  - BOL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-02-14'
temporal_resolution: null
title: Satellite detected waters over El Beni department, Bolivia
version: null
vulnerability: null
---
