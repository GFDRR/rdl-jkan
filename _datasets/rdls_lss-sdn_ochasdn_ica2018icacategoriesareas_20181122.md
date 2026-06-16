---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP GeoNode
    url: https://data.humdata.org/dataset/ica-sudan-2018-ica-categories-areas
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/ica-sudan-2018-ica-categories-areas
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/ica-sudan-2018-ica-categories-areas
dataset_id: rdls_lss-sdn_ochasdn_ica2018icacategoriesareas_20181122
description: 'This layer contains information about the final categorization resulting
  from the Integrated Context Analysis (ICA) performed in Sudan in 2018, showing the
  areas of convergence of high levels of food insecurity recurrence and major propensity
  to natural shocks (floods and droughts).. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ica-sudan-2018-ica-categories-areas]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: The ICA Sudan 2018 dataset integrates food insecurity classification
    data with hazard propensity assessments for floods and droughts at the administrative
    level 2 (district) scale. The analysis identifies geographic areas where high
    recurrence of food insecurity converges with major propensity to natural shocks,
    producing categorized risk zones for humanitarian planning and resource allocation.
  sources:
  - id: source_1
    license: null
    name: WFP GeoNode
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ica-sudan-2018-ica-categories-areas
  rel: source
loss:
  losses:
  - asset_category: economic_indicator
    asset_dimension: index
    description: Food insecurity classification linked to flood hazard propensity
      in Sudan administrative areas
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: exposure
        modelling: observed
        type: indirect
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: economic_indicator
    asset_dimension: index
    description: Food insecurity classification linked to drought hazard propensity
      in Sudan administrative areas
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: exposure
        modelling: observed
        type: indirect
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Sample Survey
referenced_by: []
resources:
- access_url: https://geonode.wfp.org/geoserver/wfs?format_options=charset%3AUTF-8&typename=geonode%3Asdn_ica_categories_areas_geonode_20180201&outputFormat=SHAPE-ZIP&version=1.0.0&service=WFS&request=GetFeature
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: This layer contains information about the final categorization resulting
    from the Integrated Context Analysis (ICA) performed in Sudan in 2018, showing
    the areas of convergence of high levels of food insecurity recurrence and major
    propensity to natural shocks (floods and droughts).
  download_url: null
  format: null
  id: resource_28a25171
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sudan, 2018 - ICA Categories & Areas
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_ochasdn_ica2018icacategoriesareas_20181122
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-11-22'
temporal_resolution: null
title: ICA Sudan, 2018 - ICA Categories & Areas
version: null
vulnerability: null
---
