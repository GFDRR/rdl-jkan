---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: German Aerospace Center (DLR)
  url: www.dlr.de/eoc/en/desktopdefault.aspx/tabid-9628/16557_read-40454/
creator:
  affiliation: null
  email: null
  name: German Aerospace Center (DLR)
  url: www.dlr.de/eoc/en/desktopdefault.aspx/tabid-9628/16557_read-40454/
dataset_id: rdls_exp-crstac_globalurbanfootprintguf_28arcseconds
description: 'Binary settlement mask at 2.8 arc seconds resolution [Source: This metadata
  record was automatically extracted from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure:
- asset_type:
    description: urban/built-up footprints
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
      quantity_kind: area
      unit: square_metre
hazard: null
license: https://example.org/license/unknown
lineage:
  description: Provides a binary settlement mask which at a unprecedented spatial
    resolution gives a complete picture of urban and rural settlements.
  sources:
  - id: source_underlying_1
    license: null
    name: TerraSAR-X
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_underlying_2
    license: null
    name: TanDEM-X satellite imagery
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: German Aerospace Center (DLR)
  url: www.dlr.de/eoc/en/desktopdefault.aspx/tabid-9628/16557_read-40454/
purpose: 'upon request by filling in user form: https://www.dlr.de/de/eoc/downloads/dokumente/guf/DLR-GUF_LicenseAgreement-and-OrderForm.pdf/@@download/file'
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1016/j.isprsjprs.2017.10.012
  id: ref_doi
  name: null
  url: https://doi.org/10.1016/j.isprsjprs.2017.10.012
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/land-use/global-urban-footprint-guf/28-arc-seconds/28-arc-seconds.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Item metadata record for this dataset, hosted as part of
    the climate-risk-stac catalogue. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_item
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Item: Global Urban Footprint (GUF) - 2.8 arc seconds'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Urban Footprint (GUF) - 2.8 arc seconds (www.dlr.de/eoc/en/desktopdefault.aspx/tabid-9628/16557_read-40454/)
  download_url: www.dlr.de/eoc/en/desktopdefault.aspx/tabid-9628/16557_read-40454/
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: www.dlr.de/eoc/en/desktopdefault.aspx/tabid-9628/16557_read-40454/
- access_url: https://doi.org/10.1016/j.isprsjprs.2017.10.012
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Urban Footprint (GUF) - 2.8 arc seconds (Web reference)
  download_url: null
  format: Web reference
  id: resource_link_reference
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Reference
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-crstac_globalurbanfootprintguf_28arcseconds
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
spatial_resolution: 86
temporal:
  central_year: null
  duration: null
  end: '2012'
  start: '2012'
temporal_resolution: null
title: Global Urban Footprint (GUF) - 2.8 arc seconds
version: null
vulnerability: null
---
