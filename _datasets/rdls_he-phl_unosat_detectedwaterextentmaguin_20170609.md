---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-maguindanao-and-cotabato-provinces-phillipines
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-maguindanao-and-cotabato-provinces-phillipines
dataset_id: rdls_he-phl_unosat_detectedwaterextentmaguin_20170609
description: 'This map illustrates the satellite-detected water extent in Maguindanao
  and Cotabato provinces, Phillipines. The UNITAR-UNOSAT analysis used a Sentinel-1
  satellite image acquired on the 07 June 2017 and could observe areas with standing
  waters mainly affecting agricultural fields. Within the map extent, the UNITAR-UNOSAT
  analysis identified ~34,000 ha of those areas and ~127 km of potentially affected
  road mainly local roads. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-in-maguindanao-and-cotabato-provinces-phillipines]'
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
    description: Agricultural fields affected by standing water, approximately 34,000
      hectares
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
    description: Road network affected by flooding, approximately 127 km of local
      roads
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
hazard:
  event_sets_by_hazard_type:
    flood:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed Sentinel-1 satellite imagery acquired on
    7 June 2017, comparing multi-temporal images to detect standing water extent and
    identify affected agricultural areas and road networks in Maguindanao and Cotabato
    provinces, Philippines. The analysis identified approximately 34,000 hectares
    of water-affected agricultural land and 127 km of potentially affected roads through
    visual interpretation of radar imagery.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-in-maguindanao-and-cotabato-provinces-phillipines
  rel: source
loss:
  losses: []
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
  description: Philippines - Satellite Detected Water Extent in Maguindanao and Cotabato
    Provinces, Phillipines (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PH/FL20170607PHL/FL20170607PHL_gdb.zip
  format: Geodatabase
  id: resource_59b8e68d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170607PHL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Satellite Detected Water Extent in Maguindanao and Cotabato
    Provinces, Phillipines (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PH/FL20170607PHL/FL20170607PHL_SHP.zip
  format: null
  id: resource_2606ef81
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170607PHL_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-phl_unosat_detectedwaterextentmaguin_20170609
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
  start: '2017-06-09'
temporal_resolution: null
title: Philippines - Satellite Detected Water Extent in Maguindanao and Cotabato Provinces,
  Phillipines
version: null
vulnerability: null
---
