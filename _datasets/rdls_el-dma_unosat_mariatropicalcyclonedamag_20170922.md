---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian OpenStreetMap
    url: https://data.humdata.org/dataset/maria-tropical-cyclone-damage-assessment-in-roseau-south-saint-georges-parish-dominica
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNOSAT
    url: https://data.humdata.org/dataset/maria-tropical-cyclone-damage-assessment-in-roseau-south-saint-georges-parish-dominica
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/maria-tropical-cyclone-damage-assessment-in-roseau-south-saint-georges-parish-dominica
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/maria-tropical-cyclone-damage-assessment-in-roseau-south-saint-georges-parish-dominica
dataset_id: rdls_el-dma_unosat_mariatropicalcyclonedamag_20170922
description: 'This map illustrates potentially damaged structures and buildings in
  South Roseau (Saint Georges Parish) as detected by satellite image acquired after
  landfall of the Tropical Cyclone Maria-17 on 19 September 2017. UNITAR-UNOSAT analysis
  used a Pleiades image acquired on 21 September 2017 as post imagery. UNITAR-UNOSAT
  identified in the analysed area Roseau South (Castle Comfort, Citronnier and Loubiere)
  863 potentially damaged structures. Taking into account the pre-building footprints
  provided by Humanitarian OpenStreetMap, this represents about 70 % of the total
  number of structures within the analysed area. Evidences of floods and mudflow could
  be also observed in the area of Wallhouse. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/maria-tropical-cyclone-damage-assessment-in-roseau-south-saint-georges-parish-dominica]'
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
    description: Building footprints and structures in South Roseau identified from
      pre-event OpenStreetMap data
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared pre-event building footprints from Humanitarian
    OpenStreetMap with post-event Pleiades satellite imagery acquired 2 days after
    Tropical Cyclone Maria landfall (21 September 2017) to identify structural damage
    through visual change detection in South Roseau, Dominica.
  sources:
  - id: source_1
    license: null
    name: Humanitarian OpenStreetMap
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: UNOSAT
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/maria-tropical-cyclone-damage-assessment-in-roseau-south-saint-georges-parish-dominica
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from Tropical Cyclone Maria detected via satellite
      image analysis
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
  description: Maria Tropical Cyclone. Damage Assessment in Roseau South, Saint Georges
    Parish, Dominica (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DM/TC20170918DMA/TC20170918DMA_gdb.zip
  format: Geodatabase
  id: resource_a63377b3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170918DMA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Maria Tropical Cyclone. Damage Assessment in Roseau South, Saint Georges
    Parish, Dominica (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DM/TC20170918DMA/TC20170918DMA_shp.zip
  format: null
  id: resource_6b26a204
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170918DMA_shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-dma_unosat_mariatropicalcyclonedamag_20170922
spatial:
  bbox: null
  centroid: null
  countries:
  - DMA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-09-22'
temporal_resolution: null
title: Maria Tropical Cyclone. Damage Assessment in Roseau South, Saint Georges Parish,
  Dominica
version: null
vulnerability: null
---
