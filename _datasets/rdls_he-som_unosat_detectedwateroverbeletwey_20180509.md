---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-bulo-burto-districts-hiraan-region-somalia-2793
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Radarsat-2
    url: https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-bulo-burto-districts-hiraan-region-somalia-2793
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-bulo-burto-districts-hiraan-region-somalia-2793
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-bulo-burto-districts-hiraan-region-somalia-2793
dataset_id: rdls_he-som_unosat_detectedwateroverbeletwey_20180509
description: 'This map illustrates satellite-detected flood water extent over Booco
  and Hagan areas, Hiraan region, Somalia using a Radarsat-2 image acquired on 09
  May 2018. Within the extent of the map about 4,000 ha of land appear to be inundated
  and according to WorldPop data, ~22,000 people, live within the extent of this map
  about 6,500 within 100 meters distance from the flooded areas which corresponds
  to about 30% of population in this zone. It is likely that flood waters have been
  systematically underestimated along highly vegetated areas along main river banks
  and within built-up urban areas because of the special characteristics of the satellite
  data used. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to UNITAR UNOSAT.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-bulo-burto-districts-hiraan-region-somalia-2793]'
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
    description: Residential population within flood extent and within 100 meters
      of flooded areas derived from WorldPop data
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
  description: Satellite radar imagery (Radarsat-2) acquired on 09 May 2018 was analyzed
    by UNOSAT through visual interpretation and change detection to delineate flood
    water extent. The resulting inundation polygon was intersected with WorldPop gridded
    population data to estimate affected population within the flooded area and within
    100-meter proximity zones, producing a post-event flood extent and exposure assessment.
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Radarsat-2
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-bulo-burto-districts-hiraan-region-somalia-2793
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
  description: Satellite Detected Water over Belet Weyne & Bulo Burto Districts, Hiraan
    Region, Somalia (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/FL20180501SOM/FL20180501SOM_SHP.zip
  format: null
  id: resource_22af0cb3
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
slug: rdls_he-som_unosat_detectedwateroverbeletwey_20180509
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
  start: '2018-05-09'
temporal_resolution: null
title: Satellite Detected Water over Belet Weyne & Bulo Burto Districts, Hiraan Region,
  Somalia
version: null
vulnerability: null
---
