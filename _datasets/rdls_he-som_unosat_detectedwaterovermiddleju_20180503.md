---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-over-middle-juba-and-lower-juba-region-somalia-2788
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-over-middle-juba-and-lower-juba-region-somalia-2788
dataset_id: rdls_he-som_unosat_detectedwaterovermiddleju_20180503
description: 'This map illustrates satellite-detected flood water extent in the district
  of Jilib, Middle Juba, Somalia. The analysis was conducted analyzing Sentinel-1
  images acquired on the 1 May 2018. As observed from the satellite imagery, a total
  of 92,000 ha of land were inundated in the area of interest. The most affected districts
  are Saakow, with almost 38,000 ha of flooded land and southern Diinsoor, with almost
  27,000 ha. At least 20 settlements are potentially located within the flooded area.
  It is likely that flood waters have been systematically underestimated along highly
  vegetated areas along main river banks and within built-up urban areas because of
  the special characteristics of the satellite data used. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-over-middle-juba-and-lower-juba-region-somalia-2788]'
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
    description: Settlements potentially located within flooded areas
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
  description: UNOSAT analysts processed Sentinel-1 synthetic aperture radar imagery
    acquired on 1 May 2018, comparing satellite images to detect notable changes in
    water extent. The analysis identified 92,000 ha of inundated land across Jilib
    district and surrounding areas, with settlement locations extracted from the flooded
    polygons.
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
- href: https://data.humdata.org/dataset/satellite-detected-water-over-middle-juba-and-lower-juba-region-somalia-2788
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
  description: Satellite detected water over Middle Juba and Lower Juba Region, Somalia
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/FL20180501SOM/FL20180501SOM_SHP.zip
  format: null
  id: resource_50ec9998
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180501SOM_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-som_unosat_detectedwaterovermiddleju_20180503
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-05-03'
temporal_resolution: null
title: Satellite detected water over Middle Juba and Lower Juba Region, Somalia
version: null
vulnerability: null
---
