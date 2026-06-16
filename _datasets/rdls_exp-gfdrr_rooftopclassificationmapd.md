---
attributions:
- entity:
    affiliation: null
    email: tisabelle@worldbank.org
    name: Isabelle Tingzon
    url: https://issa-tingzon.github.io/
  id: '0'
  role: author
- entity:
    affiliation: null
    email: pchrzanowski@worldbank.org
    name: Pierre Chrzanowski
    url: null
  id: '1'
  role: world_bank_team_lead
catalog: null
contact_point:
  affiliation: null
  email: tisabelle@worldbank.org
  name: Isabelle Tingzon
  url: https://issa-tingzon.github.io/
creator:
  affiliation: null
  email: tisabelle@worldbank.org
  name: Isabelle Tingzon
  url: https://issa-tingzon.github.io/
dataset_id: rdls_exp-gfdrr_rooftopclassificationmapd
description: Building footprint polygons in Dominica and Saint Lucia with corresponding
  roof type and roof material attributes predicted from RGB orthophotos taken in 2018-2019,
  in the aftermath of Hurricane Maria.
details: The vector dataset depicts building footprint polygons of Dominica with corresponding
  roof type and roof material attributes. The categories for roof type are FLAT, GABLE,
  HIP, and NO ROOF, and the categories for roof material are HEALTHY METAL, IRREGULAR
  METAL, CONCRETE/CEMENT, BLUE TARPAULIN, and INCOMPLETE. The roof classification
  map was derived using a convolutional neural network (CNN) model trained on ~15,000
  labels across Dominica and Saint Lucia. The roof type and roof classification maps
  were predicted from nationwide very high-resolution RGB orthophotos with a spatial
  resolution of 20 cm/px taken in 2018-2019, in the aftermath of Hurricane Maria in
  2017. The dataset also contains the predicted probabilities per category, suffixed
  by \"_PROB\".
exposure:
- asset_type: null
  category: buildings
  id: rdls_exp-gfdrr_rooftopclassificationmapd_exp
  metrics:
  - dimension: structure
    id: rdls_exp-gfdrr_rooftopclassificationmapd_m1
    measurement:
      quantity_kind: area
      unit: null
  - dimension: structure
    id: rdls_exp-gfdrr_rooftopclassificationmapd_m2
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: CC-BY-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: Digital Earth for Resilient Housing and Infrastructure in the Caribbean
  url: null
publisher:
  affiliation: null
  email: tisabelle@worldbank.org
  name: GFDRR
  url: null
purpose: null
referenced_by:
- author_names:
  - Isabelle Tingzon
  - Nuala Margaret Cowan
  - Pierre Chrzanowski
  date_published: '2023-10-02'
  doi: null
  id: '0'
  name: Can AI help build climate resilience in the Caribbean? Let's look at housing.
  url: https://blogs.worldbank.org/sustainablecities/can-ai-help-build-climate-resilience-caribbean-lets-look-housing
- author_names:
  - Isabelle Tingzon
  - Nuala Margaret Cowan
  - Pierre Chrzanowski
  date_published: '2023-08-20'
  doi: https://doi.org/10.48550/arXiv.2307.16177
  id: '1'
  name: Fusing VHR Post-disaster Aerial Imagery and LiDAR Data for Roof Classification
    in the Caribbean
  url: https://arxiv.org/abs/2307.16177
resources:
- access_url: https://drive.google.com/file/d/15_JAPZlxHaRw9ldMqYcwEC2xAlDmVD23/view?usp=drive_link
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32620
  description: Building footprint polygons of Dominica with corresponding roof type
    and roof material attributes predicted from RGB orthophotos taken in 2018-2019,
    in the aftermath of Hurricane Maria.
  download_url: https://drive.google.com/file/d/15_JAPZlxHaRw9ldMqYcwEC2xAlDmVD23/view?usp=drive_link
  format: gpkg
  id: '0'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal:
    central_year: null
    duration: null
    end: '2019'
    start: '2018'
  temporal_resolution: null
  title: Dominica Rooftop Classification Map
- access_url: https://drive.google.com/file/d/1VjaGp_Hhh7urqJsWU3QxYHirqQzReT8y/view?usp=drive_link
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32620
  description: Building footprint polygons of Saint Lucia with corresponding roof
    type and roof material attributes predicted from RGB orthophotos taken in 2022.
  download_url: https://drive.google.com/file/d/1VjaGp_Hhh7urqJsWU3QxYHirqQzReT8y/view?usp=drive_link
  format: gpkg
  id: '1'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal:
    central_year: null
    duration: null
    end: '2022'
    start: '2022'
  temporal_resolution: null
  title: Saint Lucia Rooftop Classification Map
- access_url: https://arxiv.org/abs/2307.16177
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Accurate and up-to-date information on building characteristics is
    essential for vulnerability assessment; however, the high costs and long timeframes
    associated with conducting traditional field surveys can be an obstacle to obtaining
    critical exposure datasets needed for disaster risk management. In this work,
    we leverage deep learning techniques for the automated classification of roof
    characteristics from very high-resolution orthophotos and airborne LiDAR data
    obtained in Dominica following Hurricane Maria in 2017. We demonstrate that the
    fusion of multimodal earth observation data performs better than using any single
    data source alone. Using our proposed methods, we achieve F1 scores of 0.93 and
    0.92 for roof type and roof material classification, respectively. This work is
    intended to help governments produce more timely building information to improve
    resilience and disaster response in the Caribbean.
  download_url: null
  format: pdf
  id: '2'
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Fusing VHR Post-disaster Aerial Imagery and LiDAR Data for Roof Classification
    in the Caribbean
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-gfdrr_rooftopclassificationmapd
spatial:
  bbox: null
  centroid: null
  countries:
  - DOM
  - LCA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Rooftop classification map of Dominica and Saint Lucia
version: '1.0'
vulnerability: null
---
