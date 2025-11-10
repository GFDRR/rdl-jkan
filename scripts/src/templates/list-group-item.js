export default (data) => (
`<a href="${data.url}" class="list-group-item${data.selected ? ' active ' : ''} ${data.disabled ? 'disabled' : ''}" ${data.disabled ? 'style="pointer-events: none;"' : ""}>
  <span class="list-group-item-truncate">${data.title}</span>
  <span class="badge">${data.count}</span>
  ${data.selected ? '<span class="badge"><i class="fa fa-times"></i></span>' : ''}
</a>`
)
