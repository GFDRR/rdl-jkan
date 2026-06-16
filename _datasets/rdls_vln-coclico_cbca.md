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
dataset_id: rdls_vln-coclico_cbca
description: "Dataset describing the costs and benefits of raising coastal defenses\
  \ along the European coastline aggregated per coastal NUTS2 region (provinces),\
  \ in view of climate change. Variables are cost (\u20AC), benefit (\u20AC), cost-benefit\
  \ ratio (cbr, -) and extra benefit of raising coastal protection (eb, m) for two\
  \ different climate scenarios (RCP4.5 and RCP8.5) coupled to two types of socio-economic\
  \ growth (SSP1 - sustainability and SSP5 - fossil fuel development). This dataset\
  \ is part of the LISCOAST (https://data.jrc.ec.europa.eu/collection/LISCOAST) project.\
  \ See this article (https://doi.org/10.1038/s41467-020-15665-3) for more dataset-specific\
  \ information. Variants in the source dataset - scenarios: RCP45-SSP1, RCP85-SSP5;\
  \ lon: -9.039207141, 33.22610589 - Longitude of the centroid of the NUTS2 region\
  \ (2010 version); lat: 35.05012185, 66.24224109 - Latitude of the centroid of the\
  \ NUTS2 region (2010 version). [Source: This metadata record was automatically extracted\
  \ from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]"
details: null
exposure: []
hazard: null
license: https://example.org/license/unknown
lineage:
  description: "Dataset describing the costs and benefits of raising coastal defenses\
    \ along the European coastline aggregated per coastal NUTS2 region (provinces),\
    \ in view of climate change. Variables are cost (\u20AC), benefit (\u20AC), cost-benefit\
    \ ratio (cbr, -) and extra benefit of raising coastal protection (eb, m) for two\
    \ different climate scenarios (RCP4.5 and RCP8.5) coupled to two types of socio-economic\
    \ growth (SSP1 - sustainability and SSP5 - fossil fuel development). This dataset\
    \ is part of the LISCOAST (https://data.jrc.ec.europa.eu/collection/LISCOAST)\
    \ project. See this article (https://doi.org/10.1038/s41467-020-15665-3) for more\
    \ dataset-specific information."
  sources:
  - id: source_1
    license: null
    name: Deltares
    risk_data_type:
    - vulnerability
    type: dataset
    url: https://www.deltares.nl
    used_in: vulnerability
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
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/cbca/collection.json
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
  title: 'STAC Collection: CoCliCo - Cost benefit coastal adaptation [cbca]'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Cost benefit coastal adaptation (The root of the cbca zarr
    dataset on public Google Cloud Storage.)
  download_url: https://storage.googleapis.com/coclico-data-public/coclico/eu_coastal_adaptation.zarr
  format: null
  id: resource_data
  media_type: application/vnd.zarr
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cbca zarr root
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/assets/thumbnails/cbca.png
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Cost benefit coastal adaptation
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
- vulnerability
schema: rdls-10
slug: rdls_vln-coclico_cbca
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
title: CoCliCo - Cost benefit coastal adaptation
version: null
vulnerability: null
---
