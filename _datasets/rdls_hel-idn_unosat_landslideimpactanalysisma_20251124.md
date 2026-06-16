---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/landslide-impact-analysis-in-majenang-sub-district-cilacap-district-jawa-tengah-province-i
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-in-majenang-sub-district-cilacap-district-jawa-tengah-province-i
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-in-majenang-sub-district-cilacap-district-jawa-tengah-province-i
dataset_id: rdls_hel-idn_unosat_landslideimpactanalysisma_20251124
description: 'UNOSAT code: LS20251118IDN This map illustrates satellite-detected landslides
  in Majenang Sub-district, Cilacap District, Jawa Tengah Province, Indonesia as observed
  from a Sentinel-2 and Shengi-02 images acquired on 18 and 21 November 2025. Within
  the analysed area of 500 hectares, about 10 hectares, of landslide scars were observed.
  UNITAR-UNOSAT identified about 30 damaged buildings and 40 potentially affected
  buildings. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/landslide-impact-analysis-in-majenang-sub-district-cilacap-district-jawa-tengah-province-i]'
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
    description: Building stock in the landslide-affected area, classified as damaged
      or potentially affected
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
hazard:
  event_sets_by_hazard_type:
    landslide:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: LSI:-
        process: landslide_general
        trigger: null
        type: landslide
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery (Sentinel-2
    and Shengi-02) acquired on 18-21 November 2025 to detect landslide scars and assess
    building damage in Majenang Sub-district. Landslide extent was mapped within a
    500-hectare study area, and building damage was classified as confirmed damaged
    or potentially affected based on visual interpretation of satellite imagery.
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
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/landslide-impact-analysis-in-majenang-sub-district-cilacap-district-jawa-tengah-province-i
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from landslide impact, with 30 damaged and
      40 potentially affected buildings identified
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
  description: Landslide impact analysis in Majenang Sub-district, Cilacap District,
    Jawa Tengah Province, Indonesia as of 18 November 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4220/LS20251118IDN_gdb.zip
  format: Geodatabase
  id: resource_0d0d8c69
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20251118IDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Landslide impact analysis in Majenang Sub-district, Cilacap District,
    Jawa Tengah Province, Indonesia as of 18 November 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4220/LS20251118IDN_SHP.zip
  format: null
  id: resource_119ac8fc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20251118IDN_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-idn_unosat_landslideimpactanalysisma_20251124
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-11-24'
temporal_resolution: null
title: Landslide impact analysis in Majenang Sub-district, Cilacap District, Jawa
  Tengah Province, Indonesia as of 18 November 2025
version: null
vulnerability: null
---
