---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/flood-impact-assessment-of-vilankulo-town-inhambane-province-mozambique-as-of-13-march-202
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldView-3 satellite imagery
    url: https://data.humdata.org/dataset/flood-impact-assessment-of-vilankulo-town-inhambane-province-mozambique-as-of-13-march-202
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Pleiades satellite imagery
    url: https://data.humdata.org/dataset/flood-impact-assessment-of-vilankulo-town-inhambane-province-mozambique-as-of-13-march-202
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-of-vilankulo-town-inhambane-province-mozambique-as-of-13-march-202
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-of-vilankulo-town-inhambane-province-mozambique-as-of-13-march-202
dataset_id: rdls_hel-moz_unosat_floodimpactassessmentvila_20230315
description: 'UNOSAT code TC20230221MOZ, GDACS Id: 1000961 This map illustrates satellite-detected
  surface waters in Vilankulo Town, Inhambane Province, Mozambique as observed from
  a WorldView-3 image acquired 13 March 2023 at 09:40 local time and Pleiades image
  acquired 10 March 2023 at 09:48 local time. Within the analysis extent of about
  2,800 hectares, approximately 35 hectares of land appear to be flooded. Based on
  Worldpop population data and the detected surface waters within the analysis extent,
  approximately 350 people are potentially exposed to or living close to flooded areas
  along with 71 structures and potentially affected road 290 meter by flooding. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to United Nations Satellite Centre (UNOSAT).. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/flood-impact-assessment-of-vilankulo-town-inhambane-province-mozambique-as-of-13-march-202]'
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
  description: UNOSAT analysts compared multi-temporal satellite imagery (WorldView-3
    and Pleiades) acquired during the March 2023 flood event to detect surface water
    extent and delineate flooded areas. Detected inundation polygons (~35 hectares)
    were intersected with WorldPop gridded population data to estimate population
    exposure within the 2,800-hectare analysis extent of Vilankulo Town.
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
    name: WorldView-3 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: Pleiades satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/flood-impact-assessment-of-vilankulo-town-inhambane-province-mozambique-as-of-13-march-202
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flooding in Vilankulo Town based on satellite-detected
      inundation extent
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
  description: Flood Impact assessment of Vilankulo Town, Inhambane Province, Mozambique
    as of 13 March 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3530/TC20230221MOZ_gdb.zip
  format: Geodatabase
  id: resource_ebabadeb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230221MOZ_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood Impact assessment of Vilankulo Town, Inhambane Province, Mozambique
    as of 13 March 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3530/TC20230221MOZ_shp.zip
  format: null
  id: resource_dd87ec3f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230221MOZ_shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-moz_unosat_floodimpactassessmentvila_20230315
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
  start: '2023-03-15'
temporal_resolution: null
title: Flood Impact assessment of Vilankulo Town, Inhambane Province, Mozambique as
  of 13 March 2023
version: null
vulnerability: null
---
