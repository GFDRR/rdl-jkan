---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extents-in-mananjary-and-nosy-varika-districts-madagascar-as-of-24-february-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extents-in-mananjary-and-nosy-varika-districts-madagascar-as-of-24-february-2022
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Sentinel-2
    url: https://data.humdata.org/dataset/water-extents-in-mananjary-and-nosy-varika-districts-madagascar-as-of-24-february-2022
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-mananjary-and-nosy-varika-districts-madagascar-as-of-24-february-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-mananjary-and-nosy-varika-districts-madagascar-as-of-24-february-2022
dataset_id: rdls_hel-mdg_unosat_detectedwaterextentsmanan_20220302
description: 'UNOSAT code: TC20220221MDG This map illustrates satellite-detected surface
  waters in Mananjary and Nosy-Varika Districts, Vatovavy Fitovinany Region, Madagascar
  as observed from a Sentinel-2 image acquired on 24 February 2022 at 10:00 local
  time. Within the analyzed cloud free zones of about 800km2, a total of about 105
  km2 of lands appear to be flooded. Based on Worldpop population data and the detected
  surface waters, about 13,400 people are potentially exposed or living close to flooded
  areas. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to United Nations Satellite Centre (UNOSAT).. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-in-mananjary-and-nosy-varika-districts-madagascar-as-of-24-february-2022]'
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
    description: Estimated population potentially exposed or living close to flooded
      areas, derived from WorldPop population data intersected with detected flood
      extents
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
  - analysis_type: deterministic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: coastal_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Sentinel-2 optical satellite imagery acquired on 24 February 2022 was
    analyzed by UNOSAT analysts to detect and delineate surface water extents across
    approximately 800 km2 of cloud-free areas in Mananjary and Nosy-Varika Districts
    following Tropical Cyclone Batsirai. Detected flood polygons (totaling ~105 km2)
    were intersected with WorldPop population data to estimate the number of people
    potentially exposed to flooding. The dataset provides a preliminary, pre-field-validation
    snapshot of flood extent and population exposure for emergency response purposes.
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
  - id: source_3
    license: null
    name: Sentinel-2
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-in-mananjary-and-nosy-varika-districts-madagascar-as-of-24-february-2022
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Estimated number of people (approximately 13,400) potentially exposed
      or living close to flooded areas based on satellite-detected water extents and
      WorldPop data
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
        modelling: inferred
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
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
  description: Satellite detected water extents in Mananjary and Nosy-Varika Districts,
    Madagascar as of 24 February 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/MG/TC20220221MDG/TC20220221MDG_gdb.zip
  format: Geodatabase
  id: resource_c5dff4e9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220221MDG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Mananjary and Nosy-Varika Districts,
    Madagascar as of 24 February 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/MG/TC20220221MDG/TC20220221MDG_SHP.zip
  format: null
  id: resource_827efbe6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220221MDG_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mdg_unosat_detectedwaterextentsmanan_20220302
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
  start: '2022-03-02'
temporal_resolution: null
title: Satellite detected water extents in Mananjary and Nosy-Varika Districts, Madagascar
  as of 24 February 2022
version: null
vulnerability: null
---
