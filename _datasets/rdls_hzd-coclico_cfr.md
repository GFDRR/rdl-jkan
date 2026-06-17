---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Deltares
  url: https://www.deltares.nl
creator:
  affiliation: null
  email: null
  name: Deltares
  url: https://www.deltares.nl
dataset_id: rdls_hzd-coclico_cfr
description: 'Dataset presenting the results of a European coastal flood risk assessment
  (present till 2100), incorporating impacts of climate change scenarios (RCP4.5 and
  RCP8.5) and different socio-economic pathways (SSP1, SSP3 and SSP5). Outcomes are
  expressed in Expected Annual Damage (EAD), EAD per Gross Domestic Product (EAD_GDP)
  and the Expected Annual number of People Affected (AEPA) per NUTS0 region (country)
  and are available for the years 2000, 2050 and 2100. This dataset is part of the
  LISCOAST (https://data.jrc.ec.europa.eu/collection/LISCOAST) project. See this article
  (https://doi.org/10.1038/s41558-018-0260-4) for more dataset-specific information.
  Variants in the source dataset - scenarios: RCP4.5-SSP1, RCP8.5-SSP3, RCP8.5-SSP5;
  time: 2000, 2050, 2100; lon: -8.516135879, 33.22610589 - longitude of the centroid
  of NUTS0; lat: 35.05012185, 64.47029683 - latitude of the centroid of NUTS0. [Source:
  This metadata record was automatically extracted from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: https://example.org/license/unknown
lineage:
  description: Dataset presenting the results of a European coastal flood risk assessment
    (present till 2100), incorporating impacts of climate change scenarios (RCP4.5
    and RCP8.5) and different socio-economic pathways (SSP1, SSP3 and SSP5). Outcomes
    are expressed in Expected Annual Damage (EAD), EAD per Gross Domestic Product
    (EAD_GDP) and the Expected Annual number of People Affected (AEPA) per NUTS0 region
    (country) and are available for the years 2000, 2050 and 2100. This dataset is
    part of the LISCOAST (https://data.jrc.ec.europa.eu/collection/LISCOAST) project.
    See this article (https://doi.org/10.1038/s41558-018-0260-4) for more dataset-specific
    information.
  sources:
  - id: source_1
    license: null
    name: Deltares
    risk_data_type:
    - hazard
    type: dataset
    url: https://www.deltares.nl
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Deltares
  url: https://www.deltares.nl
purpose: null
referenced_by: []
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/cfr/collection.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Collection metadata for this dataset, hosted as part of
    the CoCliCo catalog. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_collection
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Collection: CoCliCo - Coastal flood risk [cfr]'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The root of the Expected Annual Damage zarr dataset on public Google
    Cloud Storage.
  download_url: https://storage.googleapis.com/coclico-data-public/coclico/coastal_flood_risk.zarr
  format: null
  id: resource_data
  media_type: application/vnd.zarr
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Expected Annual Damage zarr root
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/assets/thumbnails/cfr.png
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Coastal flood risk
  download_url: null
  format: null
  id: resource_thumbnail
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Thumbnail
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-coclico_cfr
spatial:
  bbox:
  - -180.0
  - -90.0
  - 180.0
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: CoCliCo - Coastal flood risk
version: null
vulnerability: null
---
